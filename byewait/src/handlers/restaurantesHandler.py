from tornado.ioloop import IOLoop
import tornado.web
import logging
from services.restaurantesService import RestaurantesService
from utils.logger import Logger
from handlers import base

logger = Logger('restaurantesHandler')

class RestaurantesHandler(base.BaseHandler):
    
    @tornado.web.asynchronous
    def get(self):
        logger.debug("restaurantesHandler get")
        svc = RestaurantesService()
        restaurantes = svc.getAllRestaurants()
        self.write({"restaurantes": restaurantes})
        self.finish()
        
    @tornado.web.asynchronous
    def post(self):
        logger.debug("restaurantesHandler post")
        svc = RestaurantesService()
        self.finish()