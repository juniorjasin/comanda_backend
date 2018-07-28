import unittest
import requests
import json
import sys

# Nota: los metodos de las clases de test DEBEN comenzar
# con el nombre 'test', sino no funciona.

class TestPedido(unittest.TestCase):

    def test_postPedidoIncorrectBody(self):
        body = '{"incorrect_parameter": 1}'
        response = requests.post("http://localhost:8888/asd/pedido", body)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_postNoBody(self):
        response = requests.post("http://localhost:8888/asd/pedido")
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_postCorrectBody(self):
        for i in range(1, 5):
            body = '{"order":{"id_restaurante":1,"items":[{"id":"1","cantidad": 3,"aclaraciones": "sin ajo"},{"id":"2","cantidad": 1,"aclaraciones": "sin queso"}]}}'
            response = requests.post("http://localhost:8888/asd/pedido", data=body)
            self.assertEqual(response.status_code, 200)

            order = json.loads(response.content)
            self.assertTrue('order' in order)
            self.assertTrue('id' in order['order'])
                

if __name__ == "__main__":
    unittest.main()