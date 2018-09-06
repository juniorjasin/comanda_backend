import unittest
import requests
import json
import sys

class TestMenu(unittest.TestCase):
    def test_menu_01(self):
        response = requests.get('http://localhost:8888/resto1/menu')
        self.assertEqual(response.status_code, 200)

class TestRestaurante(unittest.TestCase):
    def test_restaurante_01(self):
        response = requests.get('http://localhost:8888/restaurantes')
        self.assertEqual(response.status_code, 200)

class TestPedido(unittest.TestCase):
    def test_restaurante_01(self):
        response = requests.get('http://localhost:8888/resto1/pedido')
        self.assertEqual(response.status_code, 200)

class TestLogin(unittest.TestCase):
    def test_restaurante_01(self):
        response = requests.get('http://localhost:8888/login')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(res['token'])

class TestRegister(unittest.TestCase):
    def test_restaurante_01(self):
        response = requests.get('http://localhost:8888/register')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()