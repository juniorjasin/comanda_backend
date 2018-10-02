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
        logger.debug('getItem con id:{}'.format(id))
        item = None
        try:        
            cursor = self.cnx.cursor()
            query = "SELECT id_item_menu, nombre_item_menu, description, image_url, precio, rating \
                       FROM item_menu \
                      WHERE item_menu.id_item_menu = %s"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            cursor.close()
            if row is not None and len(row) > 0:
                id, name, description, image_url, price, rating = row
                if rating != None:
                    item = Item(id, name, description, image_url, price, int(rating), opciones=[])
                else:
                    item = Item(id, name, description, image_url, price, None, opciones=[])


        except Exception as e:
            msg = "Fallo la consulta de getItem a la base de datos: {}".format(e)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)
        return item

    def getAll(self):
        # TODO
        pass

        
        