from tornado.ioloop import IOLoop
import tornado.web
import logging
import json
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
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous    
    def post(self, restaurante):
        logger.debug("menuHandler post")
        data = json.loads(self.request.body)        
        id_restaurante = data['id_restaurante']
        svc = MenuService()        
        menu = svc.getItemsMenu(id_restaurante)
        self.write({"menu":menu})
        self.finish()