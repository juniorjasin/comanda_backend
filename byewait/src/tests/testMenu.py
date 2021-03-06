import unittest
import requests
import json
import sys
from test import Test

# Nota: los metodos de las clases de test DEBEN comenzar
# con el nombre 'test', sino no funciona.

class TestMenu(Test):

    def test_getItemsMenuIncorrectBody(self):
        body = '{"incorrect_parameter": 1}'
        response = requests.post("http://localhost:8888/asd/menu", body)
        content = json.loads(response.content.decode('utf-8'))
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_getItemsMenuNoBody(self):
        response = requests.post("http://localhost:8888/asd/menu")
        content = json.loads(response.content.decode('utf-8'))
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_getItemsMenuCorrectBody(self):
        for i in range(1, 2):
            body = '{"id_restaurante": '+ str(i) +'}'
            response = requests.post("http://localhost:8888/asd/menu", data=body)
            self.assertEqual(response.status_code, 200)

            menu = json.loads(response.content.decode('utf-8'))
            if menu['menu']: # menu['menu'] distinto de {}
                # print('EXISTE menu para id_restaurante:{}'.format(i))

                self.assertTrue('menu' in menu)
                self.assertTrue('style' in menu['menu'])
                self.assertTrue('categories' in menu['menu'])

                categories = menu['menu']['categories']
                for cat in categories:
                    self.assertTrue('id' in cat)
                    self.assertTrue('name' in cat)
                    self.assertTrue('image' in cat)
                    self.assertTrue('subcategorias' in cat)
                    
                    subcategorias = cat['subcategorias']
                    
                    for subcat in subcategorias:
                        self.assertTrue('id' in subcat)
                        self.assertTrue('name' in subcat)
                        self.assertTrue('items' in subcat)

                        items = subcat['items']
                        for item in items:
                            self.assertTrue('id' in item)
                            self.assertTrue('name' in item)
                            self.assertTrue('description' in item)
                            self.assertTrue('image_url' in item)
                            self.assertTrue('price' in item)
                            self.assertTrue('opciones' in item)

if __name__ == "__main__":
    unittest.main()