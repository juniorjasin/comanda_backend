import utils.globalvars
from repository import pedidoRepo
from utils.logger import Logger
from exceptions import exceptions

logger = Logger('pedirCuentaService')

class PedirCuentaService:
    def __init__(self):
        self.repo = pedidoRepo.PedidoRepo()

    def pedirCuenta(self, idRestaurante, idMesa):
        logger.debug('pedirCuenta')
        for conn in utils.globalvars.webSockConns:
            conn.conexion.reportMesaPideCuenta(idRestaurante, idMesa)
        logger.debug('salgo de pedirCuenta')

    def actualizarPedidos(self, pedidos, estado):
        logger.debug('actualizarPedidos')
        self.repo.actualizarPedidos(pedidos, estado)
        return