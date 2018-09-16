from repository import repo
from utils.logger import Logger
from exceptions import exceptions

logger = Logger('historialPedidosRepo')

class HistorialPedidosRepo(repo.Repo):
    def __init__(self):
        super(HistorialPedidosRepo, self).__init__()
    
    def validarManagerCoincideRestaurante(self, idManager, idRestaurante):        
        logger.debug('validarManagerCoincideRestaurante')
        respuesta = False 
        try:
            cursor = self.cnx.cursor()
            consulta = "SELECT id_restaurante FROM managers WHERE managers.id_manager = %s"
            cursor.execute(consulta,(idManager,))
            row = cursor.fetchone()
            if row is not None and idRestaurante == row[0]:
                respuesta = True
            cursor.close()
        except Exception as e:
            messg = "Fallo la consulta a la base de datos: {}".format(e)
            logger.error(messg)
            raise exceptions.InternalServerError(5001)
        return respuesta

    def getHistorialPedidos(self, idRestaurante):
        logger.debug('getHistorialPedidos')
        respuesta = {}
        try:
            cursor = self.cnx.cursor()
            consulta = "SELECT id_restaurante FROM managers WHERE managers.id_manager = %s"
            cursor.execute(consulta,(idManager,))
            row = cursor.fetchone()
            if row is not None and idRestaurante == row[0]:
                respuesta = True
            cursor.close()
        except Exception as e:
            messg = "Fallo la consulta a la base de datos: {}".format(e)
            logger.error(messg)
            raise exceptions.InternalServerError(5001)
        return respuesta