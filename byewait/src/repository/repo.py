import pymysql
import os
from utils.logger import Logger

logger = Logger('repo')


class Repo:
    def __init__(self):
        self.cnx = None
        try:
            self.cnx = pymysql.connect(db="byewait", user="dev", passwd="changeme", port=3306, host="mysql")
            logger.debug('Conexion exitosa con base de datos')
        except Exception as e:
            logger.critical(e)