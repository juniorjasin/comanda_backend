from tornado.ioloop import IOLoop
import tornado.web
import logging
from services.menuService import MenuService
from decorators.checkAuthentication import checkAuthentication
from utils.logger import Logger

logger = Logger('menuHandler')

class MenuHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, restaurante):
        logger.debug("menuHandler get")
        svc = MenuService()
        self.finish()
        
    @tornado.web.asynchronous
    @checkAuthentication
    def post(self, restaurante):
        logger.debug("menuHandler post")
        svc = MenuService()
        self.finish()