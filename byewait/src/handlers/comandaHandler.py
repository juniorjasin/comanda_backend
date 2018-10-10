from tornado.ioloop import IOLoop
import tornado.web
from utils.logger import Logger
from handlers import base
from decorators.handleException import handleException
from decorators.checkAuthentication import checkAuthentication
from services.comandaService import ComandaService
from exceptions import exceptions
import json
import utils.globalvars

logger = Logger('comandaHandler')

class ComandaHandler(base.BaseHandler):
  
    @tornado.web.asynchronous
    @handleException
    def get(self):
        logger.debug('get')       
        svc = ComandaService()
        response = svc.get_all_unfinished_comandas()
        comandas, restaurante = response
        self.finish({"comandas": comandas, "restaurante": restaurante})

    @tornado.web.asynchronous
    @handleException
    def options(self):
        self.finish()


    @tornado.web.asynchronous
    @handleException
    def post(self):
        logger.debug('post')       
        data = json.loads(self.request.body)
        id_pedido = data['id_pedido']
        nuevo_estado = data['estado']

        svc = ComandaService()
        svc.actualizarEstadoPlato(id_pedido, nuevo_estado)

        self.finish()

        
    