import unittest
import requests
import json
import sys
from test import Test

# Nota: los metodos de las clases de test DEBEN comenzar
# con el nombre 'test', sino no funciona.

# TODO: 
# Caracteres extranios en username, password y email.
class TestLogin(Test):

    def test_postIncorrectBody(self):
        body = '{"incorrect_parameter": 1}'
        response = requests.post("http://localhost:8888/login", body)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_postNoBody(self):
        response = requests.post("http://localhost:8888/login")
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_postUnauthorized(self):
        body = '{"user":{"username": "testunauthorized", "password": "testunauthorized", "email": "testunauthorized@test.com"}}'
        response = requests.post("http://localhost:8888/login", data=body)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 401)

    def test_postSuccesfulLogin(self):
        # Registrar usuario
        body = '{"user":{"username": "testcorrect", "password": "testcorrect", "email": "testcorrect@test.com"}}'
        response = requests.post("http://localhost:8888/register", data=body)
        self.assertEqual(response.status_code, 200)

        # Probar logueo
        response = requests.post("http://localhost:8888/login", data=body)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertTrue('user' in content)
        self.assertTrue('token' in content)
        self.assertTrue('id' in content['user'])
        self.assertTrue('username' in content['user'])
        self.assertTrue('password' in content['user'])

    def test_postIncorrectPassword(self):
        # Registrar usuario
        body = '{"user":{"username": "testbadpass", "password": "testbadpass", "email": "testbadpass@test.com"}}'
        response = requests.post("http://localhost:8888/register", data=body)
        self.assertEqual(response.status_code, 200)

        # Probar logueo
        body = '{"user":{"username": "testbadpass", "password": "otherpass", "email": "testbadpass@test.com"}}'
        response = requests.post("http://localhost:8888/login", data=body)
        self.assertEqual(response.status_code, 401)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
                
if __name__ == "__main__":
    unittest.main()