from tornado.ioloop import IOLoop
import tornado.web
import logging
from services import restaurantesService

logger = logging.getLogger('restaurantesHandler')
logger.setLevel(logging.DEBUG)
logger.propagate = False
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class RestaurantesHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        logger.debug("restaurantesHandler get")
        svc = restaurantesService.RestaurantesService()
        self.finish()
        
    @tornado.web.asynchronous
    def post(self):
        logger.debug("restaurantesHandler post")
        svc = restaurantesService.RestaurantesService()
        self.finish()