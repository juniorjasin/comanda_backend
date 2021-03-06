import unittest
import requests
import json
import sys
from test import Test

# Nota: los metodos de las clases de test DEBEN comenzar
# con el nombre 'test', sino no funciona.

# TODO: 
# Caracteres extranios en username, password y email.
# Enviar mas caracteres de los que la base de datos soporta varchar(20) enviar 30.
class TestRegister(Test):

    def test_postIncorrectBody(self):
        body = '{"incorrect_parameter": 1}'
        response = requests.post("http://localhost:8888/register", body)
        content = json.loads(response.content.decode('utf-8'))
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_postNoBody(self):
        response = requests.post("http://localhost:8888/register")
        content = json.loads(response.content.decode('utf-8'))
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 500)

    def test_postRepeatedUsername(self):
        # Registrar usuario
        body = '{"user":{"username": "testrepeated", "password": "testrepeated", "nombre": "test", "apellido": "test", "email": "testrepeated@test.com"}}'
        response = requests.post("http://localhost:8888/register", data=body)
        self.assertEqual(response.status_code, 200)

        # Registrar mismo usuarios
        response = requests.post("http://localhost:8888/register", data=body)
        self.assertEqual(response.status_code, 409)
        content = json.loads(response.content.decode('utf-8'))
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)

    def test_postSuccesfulRegister(self):
        body = '{"user":{"username": "success", "password": "success", "nombre": "test", "apellido": "test", "email": "success@test.com"}}'
        response = requests.post("http://localhost:8888/register", data=body)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content.decode('utf-8'))
        self.assertTrue('user' in content)
        self.assertTrue('token' in content)
        self.assertTrue('id' in content['user'])
        self.assertTrue('username' in content['user'])
        self.assertTrue('email' in content['user'])

    def test_postIncorrectEmailFormat(self):
        badFormats = ('f', 'f.com', 'f@.com', 'f@f..com', 'f@com')
        for badFormat in badFormats:
            body = '{"user":{"username": "wwq", "password": "ewqs", "nombre": "test", "apellido": "test", "email": %s}}' % badFormat
            response = requests.post("http://localhost:8888/register", data=body)
            # self.assertEqual(response.status_code, 400)
            self.assertEqual(response.status_code, 500)
            content = json.loads(response.content.decode('utf-8'))
            self.assertTrue('user_message' in content)
            self.assertTrue('code' in content)
                
if __name__ == "__main__":
    unittest.main()