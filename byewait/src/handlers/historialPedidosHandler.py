import tornado.web
import json
from decorators.handleException import handleException
from services.historialPedidosService import HistorialPedidosService
from utils.logger import Logger
from handlers import base
from exceptions import exceptions

logger = Logger('historialPedidosHandler')

class HistorialPedidosHandler(base.BaseHandler):
        
    @tornado.web.asynchronous
    @handleException
    def post(self):
        logger.debug('post')
        try:
            data = json.loads(self.request.body)
            idManager = data['data']['id_manager']
            idRestaurante = data['data']['id_restaurante']
        except Exception as e:
            logger.error('Body incorrecto, exception: : {}'.format(e) + ' body: {}'.format(self.request.body))
            raise exceptions.BadRequest(3001)
        svc = HistorialPedidosService()
        if svc.validarManagerCoincideRestaurante(idManager, idRestaurante):
            respuesta = svc.getHistorialPedidos(idRestaurante)
            self.finish({'historial_pedidos': respuesta})
        else:
            logger.error('Manager no autorizado: '.format(data))
            raise exceptions.ForbiddenException(2001)