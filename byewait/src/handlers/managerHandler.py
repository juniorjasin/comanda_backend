import tornado.web
import json
from decorators.handleException import handleException
from services.managerService import ManagerService
from utils.logger import Logger
from handlers import base
from exceptions import exceptions

logger = Logger('managerHandler')

class ManagerHandler(base.BaseHandler):

    @tornado.web.asynchronous
    @handleException
    def get(self):
        logger.debug("managerHandler get")
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self):
        logger.debug('managerHandler post')
        body = json.loads(self.request.body)
        svc = ManagerService()

        try:
            user = body['user'] 
            password = body['user']['password']
            username = body['user']['username']
            
            logger.debug('intento iniciar sesion manager:{}'.format(user))

        except Exception as ex:
            logger.error('Error, el body es incorrecto, faltan atributos')
            raise exceptions.BadRequest(3001)
            
        response = svc.validarUsuario(body['user']['username'], body['user']['password'])
        logger.debug('response:{}'.format(response))

        self.finish(response)