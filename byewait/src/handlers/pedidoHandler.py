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
    def get(self, userId):
        logger.debug('get')
        svc = PedidoService()
        logger.debug('user:{}, quiere pedidos sin finalizar'.format(userId))
        infoPedidos = svc.checkPedidoPendiente(userId)
        pedidos, id_mesa, restaurante = infoPedidos
        response = None

        if restaurante is None or id_mesa is None or pedidos is None or len(pedidos) == 0:
            response = {'message': 'no hay pedidos pendientes'}
        else:
            response = {'id_mesa':id_mesa, 'restaurante':restaurante, 'pedidos':pedidos}

        self.finish(response)

    @tornado.web.asynchronous
    @handleException
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    @checkAuthentication
    def post(self, restaurante):
        logger.debug("post")
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            idUsuario = data['order']['user']['id_user']
            nombreUser = data['order']['user']['nombre']
            apellidoUser = data['order']['user']['apellido']
            id_restaurante = data['order']['id_restaurante']
            id_mesa = data['order']['id_mesa']
            items = data['order']['items']
        except Exception as e:
            logger.error('Body incorrecto, exception: : {}'.format(e) + ' body: {}'.format(self.request.body)) 
            raise exceptions.BadRequest(4001)
        svc = PedidoService()
        pedido = svc.insertOrder(id_restaurante, items, idUsuario, id_mesa)

        # Enviar la información del pedido a los clientes del web socket
        user = {'nombre': nombreUser, 'apellido': apellidoUser}
        for conn in utils.globalvars.webSockConns:
            conn.conexion.on_message({
                'order': pedido, 
                'user': user, 
                'data': data['order'], 
                'restaurante': id_restaurante})
        self.finish({"order": pedido})
