from tornado.ioloop import IOLoop
import tornado.web
import logging
from services.restaurantesService import RestaurantesService
from utils.logger import Logger

logger = Logger('restaurantesHandler')

class RestaurantesHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        logger.debug("restaurantesHandler get")
        svc = RestaurantesService()
        self.finish()
        
    @tornado.web.asynchronous
    def post(self):
        logger.debug("restaurantesHandler post")
        svc = RestaurantesService()
        self.finish()