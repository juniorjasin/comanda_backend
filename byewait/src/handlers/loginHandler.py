import tornado.web
from decorators.handleException import handleException
from services.loginService import LoginService
from utils.logger import Logger
from handlers import base

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
        logger.debug("loginHandler post")
        svc = LoginService()
        self.finish()
        