from tornado.ioloop import IOLoop
import tornado.web
import logging
from services import registerService

logger = logging.getLogger('registerHandler')
logger.setLevel(logging.DEBUG)
logger.propagate = False
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class RegisterHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        logger.debug("registerHandler get")
        svc = registerService.RegisterService()
        self.finish()
        
    @tornado.web.asynchronous
    def post(self):
        logger.debug("registerHandler post")
        svc = registerService.RegisterService()
        self.finish()