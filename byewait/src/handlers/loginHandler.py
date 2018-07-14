import tornado.web
from decorators.checkExceptions import checkExceptions
from exceptions import exceptions
from services.loginService import LoginService
from utils.logger import Logger

logger = Logger('loginHandler')

class LoginHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @checkExceptions
    def get(self):
        logger.debug("loginHandler get")
        svc = LoginService()
        token = svc.validarUsuario()
        self.write(token)
        self.finish()
        
    @tornado.web.asynchronous
    @checkExceptions
    def post(self):
        logger.debug("loginHandler post")
        svc = LoginService()
        self.finish()
        