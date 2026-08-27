import unittest

from backend.app import STATUS


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


if __name__ == '__main__':
    unittest.main()
