from repository import repo
from utils.logger import Logger
from exceptions import  exceptions
import pymysql
from collections import namedtuple
from model.item import Item

logger = Logger('itemsRepo')

class ItemsRepo(repo.Repo):
    def __init__(self):
        super(ItemsRepo, self).__init__()
        logger.debug('ItemsRepo')

    def getItem(self, id):
        logger.debug('getItem')
        item = None
        try:        
            cursor = self.cnx.cursor()
            query = "SELECT id_item_menu, nombre_item_menu, description, image_url, precio FROM item_menu"
            cursor.execute(query)
            row = cursor.fetchone()
            cursor.close()
            if row is not None:
                id, name, description, image_url, price = row
                item = Item(id, name, description, image_url, price)
        except Exception as e:
            msg = "Fallo la consulta de getItem a la base de datos: {}".format(e)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)
        return item

    def getAll(self):
        # TODO
        pass

        
        