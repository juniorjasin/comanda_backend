import unittest
import requests
import json
import sys

# Nota: los metodos de las clases de test DEBEN comenzar
# con el nombre 'test', sino no funciona.

class TestMenu(unittest.TestCase):    
    def test_getItemsMenu(self):
        # HTTP Status Ok
        response = None
        
        for i in range(1,5):
            body = '{"id_restaurante": '+ str(i) +'}'
            response = requests.post("http://localhost:8888/asd/menu", data=body)
            self.assertEqual(response.status_code, 200)

            menu = json.loads(response.content)
            if menu['menu']: # menu['menu'] distinto de {}
                print('EXISTE menu para id_restaurante:{}'.format(i))

                self.assertTrue('menu' in menu)
                self.assertTrue('style' in menu['menu'])
                self.assertTrue('categories' in menu['menu'])
                
                categories = menu['menu']['categories']
                for cat in categories:
                    self.assertTrue('id' in cat)
                    self.assertTrue('name' in cat)
                    self.assertTrue('items' in cat)

                    items = cat['items']
                    for item in items:
                        self.assertTrue('id' in item)
                        self.assertTrue('name' in item)
                        self.assertTrue('description' in item)
                        self.assertTrue('image_url' in item)
                        self.assertTrue('price' in item)
            else:
                print('NO EXISTE menu para id_restaurante:{}'.format(i))

if __name__ == "__main__":
    unittest.main()