import unittest
import os
import sys
import tempfile
import json
import sqlite3

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

import app as app_modulo


class TestBanco(unittest.TestCase):
    """Testes basicos de conexao e criacao do banco de dados."""

    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        self.tmp.close()
        self.db_antigo = app_modulo.DB_PATH
        app_modulo.DB_PATH = self.tmp.name
        app_modulo.criar_banco()

    def tearDown(self):
        app_modulo.DB_PATH = self.db_antigo
        try:
            os.unlink(self.tmp.name)
        except OSError:
            pass

    def test_conectar_retorna_conexao(self):
        conn = app_modulo.conectar()
        self.assertIsNotNone(conn)
        self.assertEqual(conn.row_factory, sqlite3.Row)
        conn.close()

    def test_criar_banco_gera_tabela_products(self):
        conn = sqlite3.connect(self.tmp.name)
        tabelas = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='products'"
        ).fetchall()
        self.assertEqual(len(tabelas), 1)
        conn.close()

    def test_criar_banco_gera_tabela_orders(self):
        conn = sqlite3.connect(self.tmp.name)
        tabelas = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='orders'"
        ).fetchall()
        self.assertEqual(len(tabelas), 1)
        conn.close()

    def test_criar_banco_gera_tabela_order_items(self):
        conn = sqlite3.connect(self.tmp.name)
        tabelas = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='order_items'"
        ).fetchall()
        self.assertEqual(len(tabelas), 1)
        conn.close()

    def test_seed_cria_6_produtos_iniciais(self):
        conn = sqlite3.connect(self.tmp.name)
        qtd = conn.execute('SELECT COUNT(*) FROM products').fetchone()[0]
        self.assertEqual(qtd, 6)
        conn.close()

    def test_orders_possui_coluna_observation(self):
        conn = sqlite3.connect(self.tmp.name)
        cols = [r[1] for r in conn.execute('PRAGMA table_info(orders)').fetchall()]
        self.assertIn('observation', cols)
        conn.close()


class TestMapeamentoStatus(unittest.TestCase):
    """Testa o dicionario de status do pedido."""

    def test_status_1_recebido(self):
        self.assertEqual(app_modulo.STATUS[1], 'Pedido recebido')

    def test_status_2_preparacao(self):
        self.assertEqual(app_modulo.STATUS[2], 'Em preparacao')

    def test_status_3_entrega(self):
        self.assertEqual(app_modulo.STATUS[3], 'Saiu para entrega')

    def test_status_4_entregue(self):
        self.assertEqual(app_modulo.STATUS[4], 'Entregue')

    def test_quantidade_status_igual_4(self):
        self.assertEqual(len(app_modulo.STATUS), 4)


class TestApiProdutos(unittest.TestCase):
    """Testes unitarios dos endpoints de produtos."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        cls.tmp.close()
        cls.db_antigo = app_modulo.DB_PATH
        app_modulo.DB_PATH = cls.tmp.name
        app_modulo.criar_banco()
        app_modulo.app.config['TESTING'] = True
        cls.client = app_modulo.app.test_client()

    @classmethod
    def tearDownClass(cls):
        app_modulo.DB_PATH = cls.db_antigo
        try:
            os.unlink(cls.tmp.name)
        except OSError:
            pass

    def test_get_products_retorna_200_e_lista(self):
        resp = self.client.get('/api/products')
        self.assertEqual(resp.status_code, 200)
        dados = json.loads(resp.data)
        self.assertIsInstance(dados, list)
        self.assertGreater(len(dados), 0)

    def test_get_product_por_id_retorna_campos(self):
        resp = self.client.get('/api/products/1')
        self.assertEqual(resp.status_code, 200)
        p = json.loads(resp.data)
        for chave in ('id', 'name', 'description', 'price', 'category', 'image'):
            self.assertIn(chave, p)

    def test_get_product_inexistente_404(self):
        resp = self.client.get('/api/products/99999')
        self.assertEqual(resp.status_code, 404)
        self.assertIn('error', json.loads(resp.data))

    def test_post_product_cria_novo(self):
        payload = {
            'name': 'Cupcake Teste',
            'description': 'Descricao teste',
            'price': 5.50,
            'category': 'Teste',
            'image': 'https://exemplo.com/img.jpg'
        }
        resp = self.client.post('/api/products', json=payload)
        self.assertEqual(resp.status_code, 201)
        self.assertIn('id', json.loads(resp.data))

    def test_post_product_campo_faltando_retorna_400(self):
        resp = self.client.post('/api/products', json={'name': 'So nome'})
        self.assertEqual(resp.status_code, 400)
        self.assertIn('error', json.loads(resp.data))

    def test_post_product_preco_negativo_retorna_400(self):
        payload = {
            'name': 'X',
            'description': 'X',
            'price': -1,
            'category': 'X',
            'image': 'X'
        }
        resp = self.client.post('/api/products', json=payload)
        self.assertEqual(resp.status_code, 400)

    def test_put_product_atualiza(self):
        payload = {
            'name': 'Cupcake Editado',
            'description': 'Nova desc',
            'price': 12.50,
            'category': 'Nova Cat',
            'image': 'https://exemplo.com/nova.jpg'
        }
        resp = self.client.put('/api/products/2', json=payload)
        self.assertEqual(resp.status_code, 200)
        r = self.client.get('/api/products/2')
        self.assertEqual(json.loads(r.data)['name'], 'Cupcake Editado')

    def test_put_product_inexistente_404(self):
        resp = self.client.put('/api/products/9999', json={})
        self.assertEqual(resp.status_code, 404)

    def test_delete_product_remover(self):
        resp = self.client.delete('/api/products/3')
        self.assertEqual(resp.status_code, 200)
        resp2 = self.client.get('/api/products/3')
        self.assertEqual(resp2.status_code, 404)

    def test_delete_product_inexistente_404(self):
        resp = self.client.delete('/api/products/9999')
        self.assertEqual(resp.status_code, 404)


class TestApiPedidos(unittest.TestCase):
    """Testes unitarios dos endpoints de pedidos."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        cls.tmp.close()
        cls.db_antigo = app_modulo.DB_PATH
        app_modulo.DB_PATH = cls.tmp.name
        app_modulo.criar_banco()
        app_modulo.app.config['TESTING'] = True
        cls.client = app_modulo.app.test_client()

    @classmethod
    def tearDownClass(cls):
        app_modulo.DB_PATH = cls.db_antigo
        try:
            os.unlink(cls.tmp.name)
        except OSError:
            pass

    def pedido_padrao(self):
        return {
            'customer_name': 'Maria Silva',
            'phone': '11999998888',
            'address': 'Rua das Flores',
            'number': '123',
            'complement': 'Apto 2',
            'neighborhood': 'Centro',
            'payment_method': 'Pix',
            'observation': 'Entregar sem cobertura de morango',
            'total': 26.00,
            'items': [
                {'product_id': 1, 'quantity': 2, 'price': 8.50},
                {'product_id': 4, 'quantity': 1, 'price': 9.00}
            ]
        }

    def test_criar_pedido_retorna_201(self):
        resp = self.client.post('/api/orders', json=self.pedido_padrao())
        self.assertEqual(resp.status_code, 201)
        self.assertIn('id', json.loads(resp.data))

    def test_criar_pedido_campo_obrigatorio_falta_400(self):
        d = self.pedido_padrao()
        del d['customer_name']
        resp = self.client.post('/api/orders', json=d)
        self.assertEqual(resp.status_code, 400)

    def test_criar_pedido_carrinho_vazio_400(self):
        d = self.pedido_padrao()
        d['items'] = []
        resp = self.client.post('/api/orders', json=d)
        self.assertEqual(resp.status_code, 400)

    def test_criar_pedido_salva_observation(self):
        d = self.pedido_padrao()
        d['observation'] = 'Teste obs OK'
        resp = self.client.post('/api/orders', json=d)
        pid = json.loads(resp.data)['id']
        r2 = self.client.get(f'/api/orders/{pid}')
        self.assertEqual(json.loads(r2.data)['observation'], 'Teste obs OK')

    def test_buscar_pedido_por_id(self):
        pid = json.loads(self.client.post('/api/orders', json=self.pedido_padrao()).data)['id']
        resp = self.client.get(f'/api/orders/{pid}')
        self.assertEqual(resp.status_code, 200)
        dados = json.loads(resp.data)
        self.assertEqual(dados['customer_name'], 'Maria Silva')
        self.assertIn('items', dados)
        self.assertEqual(len(dados['items']), 2)
        self.assertIn('status_text', dados)

    def test_buscar_pedido_inexistente_404(self):
        resp = self.client.get('/api/orders/99999')
        self.assertEqual(resp.status_code, 404)

    def test_listar_pedidos_retorna_lista(self):
        self.client.post('/api/orders', json=self.pedido_padrao())
        resp = self.client.get('/api/orders')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(json.loads(resp.data), list)

    def test_status_text_listagem(self):
        self.client.post('/api/orders', json=self.pedido_padrao())
        dados = json.loads(self.client.get('/api/orders').data)
        self.assertEqual(dados[0]['status_text'], 'Pedido recebido')

    def test_atualizar_status_valido(self):
        pid = json.loads(self.client.post('/api/orders', json=self.pedido_padrao()).data)['id']
        resp = self.client.put(f'/api/orders/{pid}/status', json={'status': 3})
        self.assertEqual(resp.status_code, 200)
        r2 = self.client.get(f'/api/orders/{pid}')
        self.assertEqual(json.loads(r2.data)['status'], 3)
        self.assertEqual(json.loads(r2.data)['status_text'], 'Saiu para entrega')

    def test_atualizar_status_invalido_400(self):
        pid = json.loads(self.client.post('/api/orders', json=self.pedido_padrao()).data)['id']
        resp = self.client.put(f'/api/orders/{pid}/status', json={'status': 99})
        self.assertEqual(resp.status_code, 400)

    def test_atualizar_status_pedido_inexistente_404(self):
        resp = self.client.put('/api/orders/9999/status', json={'status': 2})
        self.assertEqual(resp.status_code, 404)


if __name__ == '__main__':
    unittest.main(verbosity=2)
