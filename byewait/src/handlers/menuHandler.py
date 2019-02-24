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
        logger.debug('get')
        svc = MenuService()
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self, restaurante):
        logger.debug("post")
        try:
            # logger.debug('body:' + self.request.body.decode('utf-8'))
            body = self.request.body.decode('utf-8')
            data = json.loads(body)
            logger.debug('data:{}'.format(data))
            id_restaurante = data['id_restaurante']
        except Exception as e:
            logger.error('Body incorrecto, exception: : {}'.format(e) + ' body: {}'.format(body)) 
            raise exceptions.BadRequest(5001)
        svc = MenuService()
        menu = svc.getItemsMenu(id_restaurante)
        self.finish({"menu": menu})