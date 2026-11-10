import unittest
import os
import sqlite3
import tempfile
from unittest.mock import patch

from backend.app import STATUS, app, criar_banco


class TestStatusPedido(unittest.TestCase):

    def test_status_recebido(self):
        self.assertEqual(STATUS[1], 'Pedido recebido')

    def test_status_preparacao(self):
        self.assertEqual(STATUS[2], 'Em preparacao')

    def test_status_entrega(self):
        self.assertEqual(STATUS[3], 'Saiu para entrega')

    def test_status_entregue(self):
        self.assertEqual(STATUS[4], 'Entregue')

    def test_quantidade_status(self):
        self.assertEqual(len(STATUS), 4)


class TestAutenticacaoAdmin(unittest.TestCase):

    def setUp(self):
        self.variaveis = patch.dict(os.environ, {
            'ADMIN_USERNAME': 'admin-teste',
            'ADMIN_PASSWORD': 'senha-teste-segura'
        })
        self.variaveis.start()
        self.cliente = app.test_client()

    def tearDown(self):
        self.variaveis.stop()

    def test_rotas_administrativas_bloqueadas_sem_token(self):
        self.assertEqual(self.cliente.get('/api/orders').status_code, 401)
        self.assertEqual(self.cliente.get('/api/admin/orders/1').status_code, 401)
        self.assertEqual(self.cliente.post('/api/products', json={}).status_code, 401)
        self.assertEqual(
            self.cliente.put('/api/orders/1/status', json={'status': 2}).status_code,
            401
        )

    def test_login_emite_token_valido(self):
        resposta = self.cliente.post('/api/admin/login', json={
            'username': 'admin-teste',
            'password': 'senha-teste-segura'
        })
        self.assertEqual(resposta.status_code, 200)
        token = resposta.get_json()['token']
        sessao = self.cliente.get(
            '/api/admin/session',
            headers={'Authorization': f'Bearer {token}'}
        )
        self.assertEqual(sessao.status_code, 200)
        self.assertTrue(sessao.get_json()['authenticated'])

    def test_login_rejeita_credenciais_incorretas(self):
        resposta = self.cliente.post('/api/admin/login', json={
            'username': 'admin-teste',
            'password': 'senha-incorreta'
        })
        self.assertEqual(resposta.status_code, 401)


class TestAutenticacaoCliente(unittest.TestCase):

    def setUp(self):
        self.diretorio = tempfile.TemporaryDirectory()
        self.database = patch(
            'backend.app.DB_PATH',
            os.path.join(self.diretorio.name, 'teste.db')
        )
        self.database.start()
        criar_banco()
        self.cliente = app.test_client()
        resposta = self.cliente.post('/api/customer/register', json={
            'email': 'cliente@exemplo.com',
            'password': 'senha-segura-123'
        })
        self.assertEqual(resposta.status_code, 201)
        self.token_cliente = resposta.get_json()['token']

    def tearDown(self):
        self.database.stop()
        self.diretorio.cleanup()

    def test_login_e_validacao_da_sessao(self):
        resposta = self.cliente.post('/api/customer/login', json={
            'email': 'CLIENTE@EXEMPLO.COM',
            'password': 'senha-segura-123'
        })
        self.assertEqual(resposta.status_code, 200)
        sessao = self.cliente.get(
            '/api/customer/session',
            headers={'Authorization': f'Bearer {resposta.get_json()["token"]}'}
        )
        self.assertEqual(sessao.status_code, 200)
        self.assertEqual(sessao.get_json()['email'], 'cliente@exemplo.com')

    def test_cadastro_rejeita_senha_curta_e_email_duplicado(self):
        senha_curta = self.cliente.post('/api/customer/register', json={
            'email': 'outra@exemplo.com',
            'password': 'curta'
        })
        email_duplicado = self.cliente.post('/api/customer/register', json={
            'email': 'cliente@exemplo.com',
            'password': 'senha-segura-456'
        })
        self.assertEqual(senha_curta.status_code, 400)
        self.assertEqual(email_duplicado.status_code, 409)

    def test_pedido_e_consultavel_apenas_pelo_cliente_dono(self):
        produtos = self.cliente.get('/api/products').get_json()
        pedido = {
            'customer_name': 'Cliente Um',
            'phone': '(11) 98765-4321',
            'address': 'Rua Teste',
            'number': '10',
            'complement': '',
            'neighborhood': 'Centro',
            'payment_method': 'Pix',
            'observation': '',
            'total': produtos[0]['price'],
            'items': [{
                'product_id': produtos[0]['id'],
                'quantity': 1,
                'price': produtos[0]['price']
            }]
        }
        resposta = self.cliente.post('/api/orders', json=pedido, headers={
            'Authorization': f'Bearer {self.token_cliente}'
        })
        self.assertEqual(resposta.status_code, 201)
        pedido_id = resposta.get_json()['id']

        outro_cliente = self.cliente.post('/api/customer/register', json={
            'email': 'outro@exemplo.com',
            'password': 'senha-segura-456'
        }).get_json()
        outro_token = outro_cliente['token']
        lista_propria = self.cliente.get('/api/customer/orders', headers={
            'Authorization': f'Bearer {outro_token}'
        })
        pedido_alheio = self.cliente.get(
            f'/api/customer/orders/{pedido_id}',
            headers={'Authorization': f'Bearer {outro_token}'}
        )
        self.assertEqual(lista_propria.status_code, 200)
        self.assertEqual(lista_propria.get_json(), [])
        self.assertEqual(pedido_alheio.status_code, 404)

        pedido_proprio = self.cliente.get(
            f'/api/customer/orders/{pedido_id}',
            headers={'Authorization': f'Bearer {self.token_cliente}'}
        )
        self.assertEqual(pedido_proprio.status_code, 200)
        self.assertEqual(pedido_proprio.get_json()['id'], pedido_id)

    def test_criacao_e_consulta_de_pedidos_exigem_login(self):
        self.assertEqual(self.cliente.get('/api/customer/orders').status_code, 401)
        self.assertEqual(self.cliente.get('/api/orders/1').status_code, 401)
        self.assertEqual(
            self.cliente.post('/api/orders', json={}).status_code,
            401
        )

    def test_migracao_mantem_pedidos_antigos_sem_vinculo(self):
        database_legado = os.path.join(self.diretorio.name, 'legado.db')
        with patch('backend.app.DB_PATH', database_legado):
            conn = sqlite3.connect(database_legado)
            conn.execute('''CREATE TABLE orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                number TEXT NOT NULL,
                complement TEXT,
                neighborhood TEXT NOT NULL,
                payment_method TEXT NOT NULL,
                total REAL NOT NULL,
                status INTEGER NOT NULL DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )''')
            conn.execute('''INSERT INTO orders (
                customer_name, phone, address, number, complement,
                neighborhood, payment_method, total
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (
                'Pedido legado', '11999999999', 'Rua antiga', '1',
                '', 'Centro', 'Pix', 20.0
            ))
            conn.commit()
            conn.close()

            criar_banco()

            conn = sqlite3.connect(database_legado)
            pedido = conn.execute(
                'SELECT customer_name, observation, customer_id FROM orders WHERE id = 1'
            ).fetchone()
            conn.close()
        self.assertEqual(pedido, ('Pedido legado', None, None))


if __name__ == '__main__':
    unittest.main()
