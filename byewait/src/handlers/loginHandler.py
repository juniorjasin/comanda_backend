import tornado.web
import logging
from decorators.checkExceptions import checkExceptions
from exceptions import exceptions
from services.loginService import LoginService

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
    @checkExceptions
    def get(self):
        logger.debug("loginHandler get")
        svc = LoginService()
        self.finish()
        
    @tornado.web.asynchronous
    @checkExceptions
    def post(self):
        logger.debug("loginHandler post")
        svc = LoginService()
        self.finish()
        