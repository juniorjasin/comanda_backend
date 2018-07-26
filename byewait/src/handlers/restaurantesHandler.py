from tornado.ioloop import IOLoop
import tornado.web
import logging
from services.restaurantesService import RestaurantesService
from utils.logger import Logger
from handlers import base
import json
from decorators.handleException import handleException

logger = Logger('restaurantesHandler')

class RestaurantesHandler(base.BaseHandler):
    
    @tornado.web.asynchronous
    @handleException
    def get(self):
        logger.debug("restaurantesHandler get")
        svc = RestaurantesService()
        restaurantes = svc.getAllRestaurants()
        self.write({"restaurantes": restaurantes})
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self):
        logger.debug("restaurantesHandler post")
        svc = RestaurantesService()
        self.finish()