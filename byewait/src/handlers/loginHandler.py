import tornado.web
import json
from decorators.handleException import handleException
from services.loginService import LoginService
from utils.logger import Logger
from handlers import base
from exceptions import exceptions
from tornado import gen

logger = Logger('loginHandler')

class LoginHandler(base.BaseHandler):

    @tornado.web.asynchronous
    @handleException
    def get(self):
        logger.debug('get')
        svc = LoginService()
        token = svc.validarUsuario()
        self.write(token)
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self):
        logger.debug('post')
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            username = data['user']['username']
            password = data['user']['password']
            
        except Exception as e:
            logger.error('Exception: : {}'.format(e))
            raise exceptions.BadRequest(3001)

        svc = LoginService()
        respuesta = svc.validarUsuario(username, password)
        self.finish(respuesta)