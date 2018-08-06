import json
from repository import pedidoRepo
from exceptions import exceptions
from utils.logger import Logger

logger = Logger('pedidoService')

class PedidoService:
    def __init__(self):
        self.repo = pedidoRepo.PedidoRepo()

    def insertOrder(self, id_restaurante, items, id_usuario, id_mesa):
        logger.debug('insertOrder')
        order = self.repo.insertNewOrder(id_restaurante, items, id_usuario, id_mesa)
        return order