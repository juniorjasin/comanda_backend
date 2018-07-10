from tornado.ioloop import IOLoop
import tornado.web
import logging
from services import pedidoService

logger = logging.getLogger('pedidoHandler')
logger.setLevel(logging.DEBUG)
logger.propagate = False
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class PedidoHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, restaurante):
        logger.debug("pedidoHandler get")
        svc = pedidoService.PedidoService()
        self.finish()
        
    @tornado.web.asynchronous
    def post(self, restaurante):
        logger.debug("pedidoHandler post")
        svc = pedidoService.PedidoService()
        self.finish()