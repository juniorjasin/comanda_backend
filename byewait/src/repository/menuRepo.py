from repository import repo
from utils.logger import Logger
from exceptions import  exceptions
import pymysql
from model.item import Item
from model.categoria import Categoria

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
            cursor.execute("select categorias.id_categoria, categorias.nombre_categoria, categorias.imagen_categoria, item_menu.id_item_menu, item_menu.nombre_item_menu, item_menu.description, item_menu.image_url, item_menu.precio, item_menu.rating \
                     from item_menu join categorias on item_menu.id_categoria = categorias.id_categoria \
                     where item_menu.id_restaurante = %s \
                     ORDER BY categorias.id_categoria ASC",(id,))
            rows = cursor.fetchall()
            cursor.close()
            if rows == None or len(rows) == 0:
                return menu
            items = []
            categorias = []
            for index, row in enumerate(rows):
            	idCategoria, nombreCategoria, imagenCategoria, idItemMenu, nombreItemMenu, \
            	descriptionItemMenu, imageUrlItemMenu, precioItemMenu, ratingItemMenu \
            	= row
            	# Si viene null no le aplico float
            	ratingItemMenu = float(ratingItemMenu) if ratingItemMenu != None else ratingItemMenu

            	items.append(Item(id=idItemMenu, name=nombreCategoria, 
            		description=descriptionItemMenu, image_url=imageUrlItemMenu, 
            		price=float(precioItemMenu), rating=ratingItemMenu)._asdict())

            	if index + 1 == len(rows) or idCategoria != rows[index + 1][0]:
            		categorias.append(Categoria(
            	        	id=idCategoria, name=nombreCategoria, image=imagenCategoria, items=items)._asdict())
            		items = []
            menu = {
                "style":{  
                    "font-family":"Helvetica",
                    "background-color":"#00ff00"
                },
                "categories": categorias
            }
        except Exception as e:
            msg = "Fallo la consulta de getItemsMenu a la base de datos: {}".format(e)
            logger.error(msg)
            raise exceptions.InternalServerError(5002)
        return menu