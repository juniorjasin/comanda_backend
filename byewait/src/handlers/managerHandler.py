import tornado.web
import json
from decorators.handleException import handleException
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
        respuesta = {"user":{"id": 201,"username":"newuser","id_restaurante":1},"token":"...."}

        # try: # Ver si el body está bien
        #     data = json.loads(self.request.body)
        #     username = data['user']['username']
        #     password = data['user']['password']
        #     username.encode('latin-1')
        #     password.encode('latin-1')
        # except:
        #     logger.error('Error, el body es incorrecto, faltan atributos')
        #     raise exceptions.BadRequest(3001)
        # svc = LoginService()
        # respuesta = svc.validarUsuario(username,password)
        self.finish(respuesta)