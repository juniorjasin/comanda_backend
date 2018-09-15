from utils.logger import Logger
import utils.globalvars

logger = Logger('pedirCuentaService')

class PedirCuentaService:
    def pedirCuenta(self, idRestaurante, idMesa):
        logger.debug('pedirCuenta')
        for conn in utils.globalvars.webSockConns:
            conn.conexion.reportMesaPideCuenta(idRestaurante, idMesa)