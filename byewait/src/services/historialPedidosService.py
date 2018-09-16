from repository.historialPedidosRepo import HistorialPedidosRepo
import jwt
import datetime
import os
import Crypto.PublicKey.RSA as RSA
from utils.logger import Logger

logger = Logger('historialPedidosService')

class HistorialPedidosService:
    def __init__(self):
        pass
        self.repo = HistorialPedidosRepo()

    def validarManagerCoincideRestaurante(self, idManager, idRestaurante):
        logger.debug('validarManagerCoincideRestaurante')
        logger.debug(__name__)
        return self.repo.validarManagerCoincideRestaurante(idManager, idRestaurante)

    def getHistorialPedidos(self, idRestaurante):
        logger.debug('getHistorialPedidos')
        return self.repo.getHistorialPedidos(idRestaurante)
