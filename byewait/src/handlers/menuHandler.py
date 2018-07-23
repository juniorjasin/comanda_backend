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
    @checkAuthentication
    def post(self, restaurante):
        logger.debug("menuHandler post")
        svc = MenuService()
        self.finish()