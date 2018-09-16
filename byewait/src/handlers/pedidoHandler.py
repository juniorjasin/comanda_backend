from tornado.ioloop import IOLoop
import tornado.web
from services.pedidoService import PedidoService
from utils.logger import Logger
from handlers import base
from decorators.handleException import handleException
from decorators.checkAuthentication import checkAuthentication
from exceptions import exceptions
import json
import utils.globalvars

logger = Logger('pedidoHandler')

class PedidoHandler(base.BaseHandler):
  
    @tornado.web.asynchronous
    @handleException
    def get(self, restaurante):
        logger.debug('get')
        svc = PedidoService()
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    @checkAuthentication
    def post(self, restaurante):
        logger.debug("post")
        id_usuario = 1
        try:
            data = json.loads(self.request.body)
            id_restaurante = data['order']['id_restaurante']
            id_mesa = data['order']['id_mesa']
            items = data['order']['items']
        except Exception as e:
            logger.error('Body incorrecto, exception: : {}'.format(e) + ' body: {}'.format(self.request.body)) 
            raise exceptions.BadRequest(4001)
        svc = PedidoService()
        pedido = svc.insertOrder(id_restaurante, items, id_usuario, id_mesa)
        # Enviar la información del pedido a los clientes del web socket
        for conn in utils.globalvars.webSockConns:
            logger.debug('conexion:{}'.format(conn))
            conn.conexion.on_message({'order': pedido, 'data': data['order'], 'restaurante':id_restaurante})
        self.finish({"order": pedido})
