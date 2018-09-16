import unittest
import requests
import json
import sys
from test import Test
import jwt
import os

# Nota: los metodos de las clases de test DEBEN comenzar
# con el nombre 'test', sino no funciona.

private_key_file = os.path.join(os.environ['INSTALL_DIR'], 'keys','byewaitKeyy')
with open(private_key_file, 'r') as fd:
    private_key = fd.read()
payload = {'userName': 'test'}
token = jwt.encode(payload, private_key, algorithm='RS256').decode('utf-8')

class TestPedirCuenta(Test):

    def test_PedirCuentaNoAuth(self):
        body = '{"incorrect_parameter": 1}'
        response = requests.post("http://localhost:8888/resto/cuenta/pedir", data=body)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 401)

    def test_PedirCuentaIncorrectBody(self):
        body = '{"incorrect_parameter": 1}'
        headers = {'Authorization': token}
        response = requests.post("http://localhost:8888/resto/cuenta/pedir", data=body, headers=headers)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_PedirCuentaNoBody(self):
        headers = {'Authorization': token}
        response = requests.post("http://localhost:8888/resto/cuenta/pedir", headers=headers)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_PedirCuentaCorrectBody(self):
        body = '{"cuenta": {"id_restaurante": 1, "id_mesa": 1}}'
        headers = {'Authorization': token}
        response = requests.post("http://localhost:8888/resto/cuenta/pedir", data=body, headers=headers)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()