from tornado.ioloop import IOLoop
import tornado.web
import logging
from services.menuService import MenuService
from decorators.checkAuthentication import checkAuthentication
from utils.logger import Logger
from handlers import base

logger = Logger('menuHandler')

class MenuHandler(base.BaseHandler):
    @tornado.web.asynchronous
    def get(self, restaurante):
        logger.debug("menuHandler get")
        svc = MenuService()
        self.finish()

    @tornado.web.asynchronous
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    @checkAuthentication
    def post(self, restaurante):
        # logger.debug("menuHandler post")
        # svc = MenuService()
        menu = {
          'style': {
            'background-color': 'red'
          },
          'categories': [
            {
                'id': 1,
                'name': 'Hamburguesas',
                'items': [
                    {
                      "id": 1,
                      "name":"Hamburguesa Completa",
                      "description":"Hamburguesa con tomate, lechuga, etc",
                      "image_url":"https://cdn1.eldia.com/022018/1517677620223.jpg",
                      "price":14.99
                    },
                    {
                      "id": 2,
                      "name":"Hamburguesa Completa 2",
                      "description":"Hamburguesa con tomate, lechuga, etc",
                      "image_url":"https://cdn1.eldia.com/022018/1517677620223.jpg",
                      "price":14.99
                    }
                ]
            },
            {
                'id': 2,
                'name': 'Pizzas',
                'items': [
                    {
                      "id": 3,
                      "name":"Pizza Completa",
                      "description":"Pizza con tomate, lechuga, etc",
                      "image_url":"https://cdn1.eldia.com/022018/1517677620223.jpg",
                      "price":14.99
                    }
                ]
            }
          ]
        }
        self.finish({"menu": menu})