import unittest
import os
from unittest.mock import patch

from backend.app import STATUS, app


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


if __name__ == '__main__':
    unittest.main()
