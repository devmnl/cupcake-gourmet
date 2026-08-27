from flask import Flask, request, jsonify
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app)

database.create_tables()
database.seed_products()

STATUS_MESSAGES = {
    1: 'Pedido recebido',
    2: 'Em preparação',
    3: 'Saiu para entrega',
    4: 'Entregue'
}


@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        conn = database.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        conn.close()
        return jsonify([dict(p) for p in products])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        conn = database.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
        product = cursor.fetchone()
        conn.close()
        if product is None:
            return jsonify({'error': 'Produto não encontrado'}), 404
        return jsonify(dict(product))
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        if not all(k in data for k in ('name', 'description', 'price', 'category', 'image')):
            return jsonify({'error': 'Campos obrigatórios faltando'}), 400
        if data['price'] <= 0:
            return jsonify({'error': 'Preço deve ser maior que zero'}), 400

        conn = database.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO products (name, description, price, category, image) VALUES (?, ?, ?, ?, ?)',
            (data['name'], data['description'], data['price'], data['category'], data['image'])
        )
        conn.commit()
        product_id = cursor.lastrowid
        conn.close()

        return jsonify({'id': product_id, 'message': 'Produto cadastrado com sucesso'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()
        if not all(k in data for k in ('name', 'description', 'price', 'category', 'image')):
            return jsonify({'error': 'Campos obrigatórios faltando'}), 400
        if data['price'] <= 0:
            return jsonify({'error': 'Preço deve ser maior que zero'}), 400

        conn = database.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM products WHERE id = ?', (product_id,))
        if cursor.fetchone() is None:
            conn.close()
            return jsonify({'error': 'Produto não encontrado'}), 404

        cursor.execute(
            'UPDATE products SET name = ?, description = ?, price = ?, category = ?, image = ? WHERE id = ?',
            (data['name'], data['description'], data['price'], data['category'], data['image'], product_id)
        )
        conn.commit()
        conn.close()

        return jsonify({'message': 'Produto atualizado com sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        conn = database.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM products WHERE id = ?', (product_id,))
        if cursor.fetchone() is None:
            conn.close()
            return jsonify({'error': 'Produto não encontrado'}), 404

        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Produto excluído com sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/orders', methods=['GET'])
def get_orders():
    try:
        conn = database.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM orders ORDER BY created_at DESC')
        orders = cursor.fetchall()
        result = []
        for order in orders:
            order_dict = dict(order)
            order_dict['status_text'] = STATUS_MESSAGES.get(order_dict['status'], 'Desconhecido')
            result.append(order_dict)
        conn.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        conn = database.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM orders WHERE id = ?', (order_id,))
        order = cursor.fetchone()
        if order is None:
            conn.close()
            return jsonify({'error': 'Pedido não encontrado'}), 404

        order_dict = dict(order)
        order_dict['status_text'] = STATUS_MESSAGES.get(order_dict['status'], 'Desconhecido')

        cursor.execute('''
            SELECT oi.*, p.name, p.image
            FROM order_items oi
            JOIN products p ON oi.product_id = p.id
            WHERE oi.order_id = ?
        ''', (order_id,))
        items = cursor.fetchall()
        order_dict['items'] = [dict(i) for i in items]
        conn.close()

        return jsonify(order_dict)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/orders', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        required = ['customer_name', 'phone', 'address', 'number', 'neighborhood', 'payment_method', 'total', 'items']
        if not all(k in data for k in required):
            return jsonify({'error': 'Campos obrigatórios faltando'}), 400
        if len(data['items']) == 0:
            return jsonify({'error': 'Carrinho vazio'}), 400
        if data['total'] <= 0:
            return jsonify({'error': 'Total inválido'}), 400

        conn = database.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            '''INSERT INTO orders (customer_name, phone, address, number, complement, neighborhood, payment_method, total, status)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1)''',
            (
                data['customer_name'],
                data['phone'],
                data['address'],
                data['number'],
                data.get('complement', ''),
                data['neighborhood'],
                data['payment_method'],
                data['total']
            )
        )
        order_id = cursor.lastrowid

        for item in data['items']:
            cursor.execute(
                'INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)',
                (order_id, item['product_id'], item['quantity'], item['price'])
            )

        conn.commit()
        conn.close()

        return jsonify({'id': order_id, 'message': 'Pedido criado com sucesso'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/orders/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    try:
        data = request.get_json()
        if 'status' not in data:
            return jsonify({'error': 'Status é obrigatório'}), 400
        new_status = data['status']
        if new_status not in (1, 2, 3, 4):
            return jsonify({'error': 'Status inválido'}), 400

        conn = database.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM orders WHERE id = ?', (order_id,))
        if cursor.fetchone() is None:
            conn.close()
            return jsonify({'error': 'Pedido não encontrado'}), 404

        cursor.execute('UPDATE orders SET status = ? WHERE id = ?', (new_status, order_id))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Status atualizado com sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
