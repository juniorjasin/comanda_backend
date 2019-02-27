import pymysql
from exceptions import exceptions
from utils.logger import Logger

logger = Logger('repo')

class Repo:
    def __init__(self):
        self.cnx = None
        try:
            self.cnx = pymysql.connect(db="byewait", user="dev", passwd="changeme", port=3307, host="mysql")
            logger.debug('Conexion exitosa con base de datos')
        except Exception as e:
            logger.critical('No se pudo conectar con la base de datos:{}'.format(e))
            raise exceptions.InternalServerError(5001)
