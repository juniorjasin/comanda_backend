import unittest
import requests
import json
import sys
from test import Test

# Nota: los metodos de las clases de test DEBEN comenzar
# con el nombre 'test', sino no funciona.

class TestRestaurante(Test):    
      
    def test_getAllRestaurants(self):
        response = requests.get('http://localhost:8888/restaurantes')
        self.assertEqual(response.status_code, 200)

        restaurantes = json.loads(response.content.decode('utf-8'))
        
        self.assertIsNotNone(restaurantes['restaurantes'])
        listOfRestaurants = restaurantes['restaurantes']
        for l in listOfRestaurants:
            self.assertIsNotNone(l['id'])
            self.assertIsNotNone(l['name'])
            self.assertIsNotNone(l['description'])
            self.assertIsNotNone(l['image_url'])
            self.assertIsNotNone(l['address'])
            self.assertIsNotNone(l['tags'])

if __name__ == "__main__":
    unittest.main()               
