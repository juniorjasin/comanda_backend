from tornado.ioloop import IOLoop
import tornado.web
import logging
from services.restaurantesService import RestaurantesService
from utils.logger import Logger
from handlers import base
import json
from exceptions import  exceptions

logger = Logger('restaurantesHandler')

class RestaurantesHandler(base.BaseHandler):
    
    @tornado.web.asynchronous
    def get(self):
        logger.debug("restaurantesHandler get")
        svc = RestaurantesService()
        try:
            restaurantes = svc.getAllRestaurants()
            self.write({"restaurantes": restaurantes})
        except Exception as e:
            msg = "Error durante svc.getAllRestaurants: {}".format(e)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)
        
        self.finish()

    @tornado.web.asynchronous
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    def post(self):
        logger.debug("restaurantesHandler post")
        svc = RestaurantesService()
        self.finish()