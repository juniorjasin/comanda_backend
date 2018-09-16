import unittest
import requests
import json
import sys
from test import Test
import pymysql
import jwt
import os

# Nota: los metodos de las clases de test DEBEN comenzar
# con el nombre 'test', sino no funciona.

private_key_file = os.path.join(os.environ['INSTALL_DIR'], 'keys','byewaitKeyy')
with open(private_key_file, 'r') as fd:
    private_key = fd.read()
payload = {'userName': 'test'}
token = jwt.encode(payload, private_key, algorithm='RS256').decode('utf-8')

class TestMenuItemScore(Test):

    def setUp(self):
        super(TestMenuItemScore, self).setUp()
        cnx = pymysql.connect(db="byewait", user="dev", passwd="changeme", port=3306, host="mysql")
        cursor = cnx.cursor()
        cursor.execute("insert into usuarios(username, nombre, apellido, email, password) values('test', 'nombretest', 'apellidotest', 'test', 'test')")
        cursor.execute("insert into categorias(nombre_categoria, imagen_categoria) values('test', 'test')")
        cursor.execute("insert into restaurants(name, description, address, image_url) values('test', 'test', 'test', 'test')")
        cursor.execute("insert into item_menu(id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url, rating) values(1, 1, 'test', 'test', 1, 'test', null)")
        cnx.commit()
        cursor.close()
        cnx.close()

    def test_postScoreIncorrectBodyParameters(self):
        body = '{"incorrect_parameter": 1}'
        headers = {'Authorization': token}
        response = requests.post("http://localhost:8888/menu/item/score", data=body, headers=headers)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_getItemsMenuNoBody(self):
        headers = {'Authorization': token}
        response = requests.post("http://localhost:8888/menu/item/score", headers=headers)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_getItemsMenuCorrectBody(self):
        body = '{"menu_item_score": {"id_item_menu": 1,"id_usuario": 1,"score": 2}}'
        headers = {'Authorization': token}
        response = requests.post("http://localhost:8888/menu/item/score", data=body, headers=headers)
        content = json.loads(response.content)
        self.assertTrue('id' in content['menu_item_score'])
        self.assertTrue('id_item_menu' in content['menu_item_score'])
        self.assertTrue('id_usuario' in content['menu_item_score'])
        self.assertTrue('score' in content['menu_item_score'])
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
