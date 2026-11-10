from flask import Flask, request, jsonify, g
from flask_cors import CORS
from functools import wraps
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer
from werkzeug.security import check_password_hash, generate_password_hash
import secrets
import sqlite3
import os
import re

app = Flask(__name__)
secret_key = os.environ.get('SECRET_KEY')
if not secret_key and (
    os.environ.get('RENDER', '').lower() == 'true'
    or os.environ.get('FLASK_ENV') == 'production'
):
    raise RuntimeError('Configure uma SECRET_KEY fixa no ambiente de producao.')
app.config['SECRET_KEY'] = secret_key or secrets.token_hex(32)
CORS(app)

DB_PATH = os.environ.get(
    'DATABASE_PATH',
    os.path.join(os.path.dirname(__file__), 'cupcake.db')
)
CUSTOMER_TOKEN_MAX_AGE = 8 * 60 * 60


def serializer_cliente():
    return URLSafeTimedSerializer(app.config['SECRET_KEY'], salt='customer-auth')


def exigir_cliente(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        esquema, _, token = request.headers.get('Authorization', '').partition(' ')
        if esquema.lower() != 'bearer' or not token:
            return jsonify({'error': 'Entre na sua conta para continuar'}), 401

        try:
            dados = serializer_cliente().loads(token, max_age=CUSTOMER_TOKEN_MAX_AGE)
        except (BadSignature, SignatureExpired):
            return jsonify({'error': 'Sessao invalida ou expirada'}), 401

        customer_id = dados.get('customer_id') if isinstance(dados, dict) else None
        if not isinstance(customer_id, int):
            return jsonify({'error': 'Sessao invalida ou expirada'}), 401

        conn = conectar()
        cliente = conn.execute(
            'SELECT id FROM customers WHERE id = ?', (customer_id,)
        ).fetchone()
        conn.close()
        if not cliente:
            return jsonify({'error': 'Sessao invalida ou expirada'}), 401

        g.customer_id = customer_id
        return func(*args, **kwargs)
    return wrapper


def token_cliente(customer_id):
    return serializer_cliente().dumps({'customer_id': customer_id})


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

    c.execute('''CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

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
        customer_id INTEGER REFERENCES customers (id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    colunas_pedidos = {
        coluna['name'] for coluna in c.execute('PRAGMA table_info(orders)').fetchall()
    }
    if 'observation' not in colunas_pedidos:
        c.execute('ALTER TABLE orders ADD COLUMN observation TEXT')
    if 'customer_id' not in colunas_pedidos:
        c.execute('ALTER TABLE orders ADD COLUMN customer_id INTEGER REFERENCES customers (id)')

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


@app.route('/api/customer/register', methods=['POST'])
def registrar_cliente():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify({'error': 'Informe e-mail e senha'}), 400

    email = str(dados.get('email', '')).strip().lower()
    senha = str(dados.get('password', ''))
    if len(email) > 254 or not re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', email):
        return jsonify({'error': 'Informe um e-mail valido'}), 400
    if len(senha) < 8 or len(senha) > 128:
        return jsonify({'error': 'A senha deve ter entre 8 e 128 caracteres'}), 400

    conn = conectar()
    try:
        cursor = conn.execute(
            'INSERT INTO customers (email, password_hash) VALUES (?, ?)',
            (email, generate_password_hash(senha))
        )
        conn.commit()
        customer_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({'error': 'Este e-mail ja possui uma conta'}), 409
    conn.close()
    return jsonify({
        'token': token_cliente(customer_id),
        'email': email
    }), 201


@app.route('/api/customer/login', methods=['POST'])
def login_cliente():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify({'error': 'Informe e-mail e senha'}), 400

    email = str(dados.get('email', '')).strip().lower()
    senha = str(dados.get('password', ''))
    if len(senha) > 128:
        return jsonify({'error': 'E-mail ou senha incorretos'}), 401
    conn = conectar()
    cliente = conn.execute(
        'SELECT id, email, password_hash FROM customers WHERE email = ?', (email,)
    ).fetchone()
    conn.close()
    if not cliente or not check_password_hash(cliente['password_hash'], senha):
        return jsonify({'error': 'E-mail ou senha incorretos'}), 401

    return jsonify({
        'token': token_cliente(cliente['id']),
        'email': cliente['email']
    })


@app.route('/api/customer/session', methods=['GET'])
@exigir_cliente
def validar_sessao_cliente():
    conn = conectar()
    cliente = conn.execute(
        'SELECT email FROM customers WHERE id = ?', (g.customer_id,)
    ).fetchone()
    conn.close()
    return jsonify({'authenticated': True, 'email': cliente['email']})


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


@app.route('/api/orders/<int:id>', methods=['GET'])
@exigir_cliente
def buscar_pedido(id):
    return obter_pedido(id, g.customer_id)


def obter_pedido(id, customer_id):
    try:
        conn = conectar()
        pedido = conn.execute(
            'SELECT * FROM orders WHERE id = ? AND customer_id = ?',
            (id, customer_id)
        ).fetchone()
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


@app.route('/api/customer/orders', methods=['GET'])
@exigir_cliente
def listar_pedidos_cliente():
    try:
        conn = conectar()
        pedidos = conn.execute(
            '''SELECT id, total, status, created_at FROM orders
               WHERE customer_id = ? ORDER BY created_at DESC''',
            (g.customer_id,)
        ).fetchall()
        resultado = []
        for pedido in pedidos:
            item = dict(pedido)
            item['status_text'] = STATUS.get(item['status'], 'Desconhecido')
            resultado.append(item)
        conn.close()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/customer/orders/<int:id>', methods=['GET'])
@exigir_cliente
def buscar_pedido_cliente(id):
    return obter_pedido(id, g.customer_id)


@app.route('/api/orders', methods=['POST'])
@exigir_cliente
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
            '''INSERT INTO orders (customer_name, phone, address, number, complement, neighborhood, payment_method, observation, total, status, customer_id)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)''',
            (d['customer_name'], d['phone'], d['address'], d['number'],
             d.get('complement', ''), d['neighborhood'], d['payment_method'],
             d.get('observation', ''), d['total'], g.customer_id)
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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
