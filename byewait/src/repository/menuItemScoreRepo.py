from repository import repo
from utils.logger import Logger
from exceptions import  exceptions
import pymysql
from collections import namedtuple
from model.scoreItem import ScoreItem

logger = Logger('menuItemScoreRepo')

class MenuItemScoreRepo(repo.Repo):
    def __init__(self):
        logger.debug('menuItemScoreRepo')
        super(MenuItemScoreRepo, self).__init__()

    def insertScore(self, idItemMenu, idUsuario, score):
        logger.debug('insertScore')
        result = None
        try:        
            cursor = self.cnx.cursor()
            query = "INSERT into scores_item_menu(id_item_menu, id_usuario, score) values (%s, %s, %s)"
            cursor.execute(query, (idItemMenu, idUsuario, score))
            self.cnx.commit()
            result = ScoreItem(
                id=cursor.lastrowid, 
                id_item_menu=idItemMenu, 
                id_usuario=idUsuario, 
                score=score)
            cursor.close()
        except Exception as e:
            msg = "Fallo la consulta de insertScore a la base de datos: {}".format(e)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)
        return result._asdict()