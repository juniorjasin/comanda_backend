from tornado.ioloop import IOLoop
import tornado.web
from services.pedidoService import PedidoService
from utils.logger import Logger

logger = Logger('pedidoHandler')

class PedidoHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, restaurante):
        logger.debug("pedidoHandler get")
        svc = PedidoService()
        self.finish()
        
    @tornado.web.asynchronous
    def post(self, restaurante):
        logger.debug("pedidoHandler post")
        svc = PedidoService()
        self.finish()