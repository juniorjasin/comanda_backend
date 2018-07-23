import unittest
import requests
import json
import sys

# Nota: los metodos de las clases de test DEBEN comenzar
# con el nombre 'test', sino no funciona.

class TestRestaurante(unittest.TestCase):    
    def test_getAllRestaurants(self):
        # HTTP Status Ok
        response = requests.get('http://localhost:8888/restaurantes')
        self.assertEqual(response.status_code, 200)

        # Siempre debe contener el objeto restaurantes
        restaurantes = json.loads(response.content)
        self.assertIsNotNone(restaurantes['restaurantes'])
        
        # Si vienen restaurantes, entonces recorro cada uno checkeando que los valores existan
        listOfRestaurants = json.loads(restaurantes['restaurantes'])
        if listOfRestaurants != None and len(listOfRestaurants) > 0:
            for l in listOfRestaurants:
                self.assertIsNotNone(l['id'])
                self.assertIsNotNone(l['name'])
                self.assertIsNotNone(l['description'])
                self.assertIsNotNone(l['image_url'])
                self.assertIsNotNone(l['address'])

if __name__ == "__main__":
    unittest.main()