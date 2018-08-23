import unittest
import requests
import json
import sys

# Nota: los metodos de las clases de test DEBEN comenzar
# con el nombre 'test', sino no funciona.

class TestMenuItemScore(unittest.TestCase):

    def test_postScoreIncorrectBodyParameters(self):
        body = '{"incorrect_parameter": 1}'
        response = requests.post("http://localhost:8888/menu/item/score", body)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_getItemsMenuNoBody(self):
        response = requests.post("http://localhost:8888/menu/item/score")
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_getItemsMenuCorrectBody(self):
      body = '{"id_item_menu": 1, "id_usuario": 1, "score": 1}'
      response = requests.post("http://localhost:8888/menu/item/score", body)
      content = json.loads(response.content)
      self.assertTrue('score' in content)
      self.assertTrue('id' in content['score'])
      self.assertTrue('id_item_menu' in content['score'])
      self.assertTrue('id_usuario' in content['score'])
      self.assertTrue('score' in content['score'])
      self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()