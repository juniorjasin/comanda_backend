from tornado.ioloop import IOLoop
import tornado.web
import logging
from services import loginService

logger = logging.getLogger('loginHandler')
logger.setLevel(logging.DEBUG)
logger.propagate = False
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class LoginHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        logger.debug("loginHandler get")
        svc = loginService.LoginService()
        token = svc.validarUsuario()
        self.write(token)
        self.finish()
        
    @tornado.web.asynchronous
    def post(self):
        logger.debug("loginHandler post")
        svc = loginService.LoginService()
        self.finish()
        