from tornado.ioloop import IOLoop
import tornado.web
from services.pedidoService import PedidoService
from utils.logger import Logger
from handlers import base
from decorators.handleException import handleException

logger = Logger('pedidoHandler')

class PedidoHandler(base.BaseHandler):

    @tornado.web.asynchronous
    @handleException
    def get(self, restaurante):
        logger.debug("pedidoHandler get")
        svc = PedidoService()
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self, restaurante):
        logger.debug("pedidoHandler post")
        svc = PedidoService()
        self.finish()