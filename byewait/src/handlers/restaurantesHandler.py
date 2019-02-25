from tornado.ioloop import IOLoop
import tornado.web
from services.restaurantesService import RestaurantesService
from utils.logger import Logger
from handlers import base
import json
from decorators.handleException import handleException
from tornado import gen

logger = Logger('restaurantesHandler')

class RestaurantesHandler(base.BaseHandler):
    
    @tornado.web.asynchronous
    @handleException
    def get(self):
        logger.debug("get")
        svc = RestaurantesService()
        restaurantes = svc.getAllRestaurants()
        self.write({"restaurantes": restaurantes})
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self):
        self.finish()
        