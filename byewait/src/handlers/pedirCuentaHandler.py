import tornado.web
import json
from decorators.handleException import handleException
from decorators.checkAuthentication import checkAuthentication
from utils.logger import Logger
from handlers import base
from exceptions import exceptions
from services.pedirCuentaService import PedirCuentaService 

logger = Logger('pedirCuentaHandler')

class PedirCuentaHandler(base.BaseHandler):

    @tornado.web.asynchronous
    @handleException
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    @checkAuthentication
    def post(self, restaurante):
        logger.debug('post')
        try:
            data = json.loads(self.request.body)
            logger.debug('body:{}'.format(data))
            # idsPedidos = data['cuenta']['ids_pedidos']
            idRestaurante = data['cuenta']['id_restaurante']
            idMesa = data['cuenta']['id_mesa']
            pedidos = data['cuenta']['pedidos']
            # if not isinstance(idsPedidos, list):
            #     raise Exception('idsPedidos no es un array')
        except Exception as e:
            logger.error('Body incorrecto, exception: : {}'.format(e) + ' body: {}'.format(self.request.body))
            raise exceptions.BadRequest(3001)
        svc = PedirCuentaService()
        svc.pedirCuenta(idRestaurante, idMesa)
        logger.debug('pedidos:{}'.format(pedidos))
        svc.actualizarPedidos(pedidos, 'finalizado')
        self.finish({'cuenta': 'pedida'})