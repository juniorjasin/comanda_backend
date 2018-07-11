from tornado.ioloop import IOLoop
import tornado.web
import logging
from services.menuService import MenuService


logger = logging.getLogger('menuHandler')
logger.setLevel(logging.DEBUG)
logger.propagate = False
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class MenuHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, restaurante):
        logger.debug("menuHandler get")
        svc = MenuService()
        self.finish()
        
    @tornado.web.asynchronous
    def post(self, restaurante):
        logger.debug("menuHandler post")
        svc = MenuService()
        self.finish()