import tornado.web
import json
from decorators.handleException import handleException
from services.loginService import LoginService
from utils.logger import Logger
from handlers import base
from exceptions import exceptions

logger = Logger('loginHandler')

class LoginHandler(base.BaseHandler):

    @tornado.web.asynchronous
    @handleException
    def get(self):
        logger.debug("loginHandler get")
        svc = LoginService()
        token = svc.validarUsuario()
        self.write(token)
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self):
        try: # Ver si el body está bien
            data = json.loads(self.request.body)
            username = data['user']['username']
            password = data['user']['password']
            username.encode('latin-1')
            password.encode('latin-1')
        except:
            logger.error('Error, el body es incorrecto, faltan atributos')
            raise exceptions.BadRequest(3001)
        svc = LoginService()
        respuesta = svc.validarUsuario(username,password)
        self.finish(respuesta)