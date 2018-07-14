from tornado.ioloop import IOLoop
import tornado.web
import json
from services import menuService
from decorators.decorator import check_authentication

from utils.logger import Logger
logger = Logger('menuHandler')

class MenuHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, restaurante):
        logger.debug("menuHandler get")
        svc = menuService.MenuService()
        self.finish()
        
    @tornado.web.asynchronous
    @check_authentication
    def post(self, restaurante):
        logger.debug("menuHandler post")
        svc = menuService.MenuService()
        self.finish()