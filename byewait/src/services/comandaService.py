import json
from repository.comandaRepo import ComandaRepo
from exceptions import exceptions
from utils.logger import Logger

logger = Logger('comandaService')

class ComandaService:
    def __init__(self):
        self.repo = ComandaRepo()

    def get_all_unfinished_comandas(self):
        comandas = self.repo.get_all_unfinished_comandas()
        return comandas

    
    def actualizarEstadoPlato(self, pedido, nuevoEstado):
        logger.debug('actualizarPedidos')
        self.repo.actualizarEstadoPlato(pedido, nuevoEstado)
        return