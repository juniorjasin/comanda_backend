from tornado.ioloop import IOLoop
import tornado.web
import logging
import json
from services.menuService import MenuService
from decorators.checkAuthentication import checkAuthentication
from utils.logger import Logger
from handlers import base
from decorators.handleException import handleException
from exceptions import exceptions

logger = Logger('menuHandler')

class MenuHandler(base.BaseHandler):
    @tornado.web.asynchronous
    @handleException
    def get(self, restaurante):
        logger.debug("menuHandler get")
        svc = MenuService()
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self, restaurante):
        logger.debug("menuHandler post")
        # Controlar entrada
        try:
            data = json.loads(self.request.body)

        except Exception as e:
            msg = "Fallo conversion body a json: {}".format(e)
            logger.error(msg)
            raise exceptions.BadRequest(5001)
        svc = MenuService()
        menu = svc.getItemsMenu(data['id_restaurante'])
        self.finish({"menu": menu})