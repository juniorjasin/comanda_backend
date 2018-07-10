import pymysql
import logging
import os
from model import dish as dishModel

logger = logging.getLogger('mysql_repo')
logger.setLevel(logging.DEBUG)
logger.propagate = False
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class Repo:
    def __init__(self):
        self.hola = 1
        self.cnx = None
        try:
            self.cnx = pymysql.connect(db="byewait", user="dev", passwd="changeme", port=3306, host="mysql")
            logger.debug(self.cnx)
        except Exception as e:
            logger.debug(e)