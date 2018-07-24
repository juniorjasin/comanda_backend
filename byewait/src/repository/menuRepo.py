from repository import repo
from utils.logger import Logger
from exceptions import  exceptions
import pymysql

logger = Logger('menuRepo')


class MenuRepo(repo.Repo):
    def __init__(self):
        super(MenuRepo, self).__init__()
        logger.debug('menuRepo')
    
    def getItemsMenu(self,id):
        logger.debug('getItemsMenu')        
        menu = {}

        try:        
            cursor = self.cnx.cursor()
            cursor.execute("select categorias.id_categoria, categorias.nombre_categoria, item_menu.id_item_menu, item_menu.nombre_item_menu, item_menu.description, item_menu.image_url, item_menu.precio \
                     from item_menu join categorias on item_menu.id_categoria = categorias.id_categoria \
                     where item_menu.id_restaurante = %s",(id,))
            rows = cursor.fetchall()
            self.cnx.commit()
            cursor.close()
            if rows == None or len(rows) == 0:     
                #logger.debug('No hay items en el menu del restaurante indicado...')
                return menu
            else:
                #logger.debug('Si hay items en el menu del restaurante indicado...')
                id_categoria = -1
                nombre_categoria = ""
                categorias = [] # array que contendra las categorias del menu con sus items
                items = [] # array que contendra los items pertenecientes a cada categoria
                try:
                    for row in rows:                        
                        if id_categoria != row[0] and items:
                            categoria_nueva = {
                                "id": id_categoria,
                                "name":nombre_categoria,
                                "items":items
                            }
                            categorias.append(categoria_nueva)
                            id_categoria = row[0]
                            nombre_categoria = row[1]
                            items = []
                            item = {
                            "id":row[2],
                            "name":row[3],
                            "description": row[4],
                            "image_url":row[5],
                            "price": row[6]
                            }
                            items.append(item)
                        else:
                            item = {
                            "id":row[2],
                            "name":row[3],
                            "description": row[4],
                            "image_url":row[5],
                            "price": row[6]
                            }
                            items.append(item)
                            id_categoria = row[0]
                            nombre_categoria = row[1]

                    categoria_nueva = {
                                "id": id_categoria,
                                "name":nombre_categoria,
                                "items":items
                            }
                    categorias.append(categoria_nueva)
                except Exception as e:
                    msg = "Fallo la creacion del array de menu: {}".format(e)
                    logger.error(msg)
                    raise exceptions.InternalServerError(5001)
        except Exception as e2:
            msg = "Fallo la consulta de getItemsMenu a la base de datos: {}".format(e2)
            logger.error(msg)
            raise exceptions.InternalServerError(5002)
        menu = {
            "style":{  
                "font-family":"Helvetica",
                "background-color":"#00ff00"
            },
            "categories": categorias
        }        
        return menu
        