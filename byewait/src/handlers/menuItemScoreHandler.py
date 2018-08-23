from tornado.ioloop import IOLoop
import tornado.web
import logging
from services.menuItemScoreService import MenuItemScoreService
from utils.logger import Logger
from handlers import base
import json
from decorators.handleException import handleException
from exceptions import exceptions

logger = Logger('menuItemScoreHandler')

class MenuItemScoreHandler(base.BaseHandler):
    @tornado.web.asynchronous
    @handleException
    def options(self):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self):
        logger.debug("menuItemScoreHandler post")
        try:
          data = json.loads(self.request.body)
          data['id_item_menu']
          data['id_usuario']
          data['score']
        except:
          raise exceptions.BadRequest(4001)
        svc = MenuItemScoreService() 
        score = svc.insertScore(data['id_item_menu'], data['id_usuario'], data['score'])
        self.finish({'score': score})