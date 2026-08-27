from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DB_PATH = os.path.join(os.path.dirname(__file__), 'cupcake.db')

STATUS = {
    1: 'Pedido recebido',
    2: 'Em preparacao',
    3: 'Saiu para entrega',
    4: 'Entregue'
}


def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def criar_banco():
    conn = conectar()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        price REAL NOT NULL,
        category TEXT NOT NULL,
        image TEXT NOT NULL
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL,
        number TEXT NOT NULL,
        complement TEXT,
        neighborhood TEXT NOT NULL,
        payment_method TEXT NOT NULL,
        observation TEXT,
        total REAL NOT NULL,
        status INTEGER NOT NULL DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    try:
        conn.execute('ALTER TABLE orders ADD COLUMN observation TEXT')
    except Exception:
        pass

    conn.commit()

    c.execute('''CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders (id),
        FOREIGN KEY (product_id) REFERENCES products (id)
    )''')

    c.execute('SELECT COUNT(*) FROM products')
    if c.fetchone()[0] == 0:
        produtos_iniciais = [
            ('Cupcake de Chocolate', 'Cupcake de chocolate com recheio e cobertura.', 8.50, 'Chocolate', 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600&auto=format&fit=crop&q=80'),
            ('Cupcake de Morango', 'Cupcake de baunilha com morango fresco.', 9.00, 'Frutas', 'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600&auto=format&fit=crop&q=80'),
            ('Cupcake Red Velvet', 'Cupcake red velvet com cream cheese.', 10.00, 'Especiais', 'https://images.unsplash.com/photo-1587668178277-295251f900ce?w=600&auto=format&fit=crop&q=80'),
            ('Cupcake de Baunilha', 'Cupcake classico de baunilha.', 7.50, 'Classicos', 'https://images.unsplash.com/photo-1519869325930-281384150729?w=600&auto=format&fit=crop&q=80'),
            ('Cupcake de Nutella', 'Cupcake com recheio de Nutella.', 11.00, 'Especiais', 'https://images.unsplash.com/photo-1562440499-64c9a111f713?w=600&auto=format&fit=crop&q=80'),
            ('Cupcake de Limao', 'Cupcake de limao siciliano.', 8.00, 'Frutas', 'https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=600&auto=format&fit=crop&q=80')
        ]
        c.executemany(
            'INSERT INTO products (name, description, price, category, image) VALUES (?, ?, ?, ?, ?)',
            produtos_iniciais
        )
    else:
        novas_imagens = {
            'Cupcake de Chocolate': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600&auto=format&fit=crop&q=80',
            'Cupcake de Morango':  'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600&auto=format&fit=crop&q=80',
            'Cupcake Red Velvet':  'https://images.unsplash.com/photo-1587668178277-295251f900ce?w=600&auto=format&fit=crop&q=80',
            'Cupcake de Baunilha': 'https://images.unsplash.com/photo-1519869325930-281384150729?w=600&auto=format&fit=crop&q=80',
            'Cupcake de Nutella':  'https://images.unsplash.com/photo-1562440499-64c9a111f713?w=600&auto=format&fit=crop&q=80',
            'Cupcake de Limao':    'https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=600&auto=format&fit=crop&q=80'
        }
        for nome, url in novas_imagens.items():
            c.execute('UPDATE products SET image = ? WHERE name = ? AND image LIKE ?', (url, nome, 'https://coresg%'))

    conn.commit()
    conn.close()


criar_banco()


@app.route('/api/products', methods=['GET'])
def listar_produtos():
    try:
        conn = conectar()
        produtos = conn.execute('SELECT * FROM products').fetchall()
        conn.close()
        return jsonify([dict(p) for p in produtos])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/products/<int:id>', methods=['GET'])
def buscar_produto(id):
    try:
        conn = conectar()
        p = conn.execute('SELECT * FROM products WHERE id = ?', (id,)).fetchone()
        conn.close()
        if not p:
            return jsonify({'error': 'Produto nao encontrado'}), 404
        return jsonify(dict(p))
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/products', methods=['POST'])
def criar_produto():
    try:
        d = request.get_json()
        if not d.get('name') or not d.get('description') or not d.get('price') or not d.get('category') or not d.get('image'):
            return jsonify({'error': 'Preencha todos os campos'}), 400
        if d['price'] <= 0:
            return jsonify({'error': 'Preco invalido'}), 400
        conn = conectar()
        c = conn.cursor()
        c.execute(
            'INSERT INTO products (name, description, price, category, image) VALUES (?, ?, ?, ?, ?)',
            (d['name'], d['description'], d['price'], d['category'], d['image'])
        )
        conn.commit()
        novo_id = c.lastrowid
        conn.close()
        return jsonify({'id': novo_id, 'message': 'Produto cadastrado'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/products/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    try:
        d = request.get_json()
        conn = conectar()
        existe = conn.execute('SELECT id FROM products WHERE id = ?', (id,)).fetchone()
        if not existe:
            conn.close()
            return jsonify({'error': 'Produto nao encontrado'}), 404
        conn.execute(
            'UPDATE products SET name=?, description=?, price=?, category=?, image=? WHERE id=?',
            (d['name'], d['description'], d['price'], d['category'], d['image'], id)
        )
        conn.commit()
        conn.close()
        return jsonify({'message': 'Produto atualizado'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/products/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    try:
        conn = conectar()
        existe = conn.execute('SELECT id FROM products WHERE id = ?', (id,)).fetchone()
        if not existe:
            conn.close()
            return jsonify({'error': 'Produto nao encontrado'}), 404
        conn.execute('DELETE FROM products WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Produto excluido'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/orders', methods=['GET'])
def listar_pedidos():
    try:
        conn = conectar()
        pedidos = conn.execute('SELECT * FROM orders ORDER BY created_at DESC').fetchall()
        resultado = []
        for p in pedidos:
            pd = dict(p)
            pd['status_text'] = STATUS.get(pd['status'], 'Desconhecido')
            resultado.append(pd)
        conn.close()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/orders/<int:id>', methods=['GET'])
def buscar_pedido(id):
    try:
        conn = conectar()
        pedido = conn.execute('SELECT * FROM orders WHERE id = ?', (id,)).fetchone()
        if not pedido:
            conn.close()
            return jsonify({'error': 'Pedido nao encontrado'}), 404
        pd = dict(pedido)
        pd['status_text'] = STATUS.get(pd['status'], 'Desconhecido')
        itens = conn.execute('''
            SELECT oi.*, p.name FROM order_items oi
            JOIN products p ON oi.product_id = p.id
            WHERE oi.order_id = ?
        ''', (id,)).fetchall()
        pd['items'] = [dict(i) for i in itens]
        conn.close()
        return jsonify(pd)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/orders', methods=['POST'])
def criar_pedido():
    try:
        d = request.get_json()
        if not d.get('customer_name') or not d.get('phone') or not d.get('address') or not d.get('number') or not d.get('neighborhood') or not d.get('payment_method') or not d.get('total') or not d.get('items'):
            return jsonify({'error': 'Preencha todos os campos'}), 400
        if len(d['items']) == 0:
            return jsonify({'error': 'Carrinho vazio'}), 400

        conn = conectar()
        c = conn.cursor()
        c.execute(
            '''INSERT INTO orders (customer_name, phone, address, number, complement, neighborhood, payment_method, observation, total, status)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1)''',
            (d['customer_name'], d['phone'], d['address'], d['number'],
             d.get('complement', ''), d['neighborhood'], d['payment_method'],
             d.get('observation', ''), d['total'])
        )
        pedido_id = c.lastrowid
        for item in d['items']:
            c.execute(
                'INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)',
                (pedido_id, item['product_id'], item['quantity'], item['price'])
            )
        conn.commit()
        conn.close()
        return jsonify({'id': pedido_id, 'message': 'Pedido criado'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/orders/<int:id>/status', methods=['PUT'])
def atualizar_status(id):
    try:
        d = request.get_json()
        novo = d.get('status')
        if novo not in (1, 2, 3, 4):
            return jsonify({'error': 'Status invalido'}), 400
        conn = conectar()
        existe = conn.execute('SELECT id FROM orders WHERE id = ?', (id,)).fetchone()
        if not existe:
            conn.close()
            return jsonify({'error': 'Pedido nao encontrado'}), 404
        conn.execute('UPDATE orders SET status = ? WHERE id = ?', (novo, id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Status atualizado'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
