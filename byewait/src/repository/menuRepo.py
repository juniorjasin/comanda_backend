from repository import repo
from utils.logger import Logger
from exceptions import  exceptions
import pymysql
from model.item import Item
from model.opcionItem import OpcionItem 
from model.detalleOpcionItem import DetalleOpcionItem 
from model.categoria import Categoria

logger = Logger('menuRepo')


class MenuRepo(repo.Repo):
	def __init__(self):
		super(MenuRepo, self).__init__()
		logger.debug('menuRepo')
	
	def getItemsMenu(self, id):
		logger.debug('getItemsMenu')        
		menu = {}

		try:        
			cursor = self.cnx.cursor()
			cursor.execute("select categorias.id_categoria, categorias.nombre_categoria, categorias.imagen_categoria, item_menu.id_item_menu, item_menu.nombre_item_menu, item_menu.description, item_menu.image_url, item_menu.precio, item_menu.rating \
					 FROM item_menu JOIN categorias on item_menu.id_categoria = categorias.id_categoria \
					 WHERE item_menu.id_restaurante = %s \
					 ORDER BY categorias.id_categoria ASC",(id,))
			rows = cursor.fetchall()
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


				cursor.execute("SELECT doim.id_opciones_item_menu, \
									   oim.nombre, \
									   doim.nombre, \
									   doim.precio, \
				             doim.nro_detalle \
								  FROM item_menu_opciones_item_menu imoim \
									  JOIN opciones_item_menu oim \
										ON imoim.id_opciones_item_menu = oim.id \
									  JOIN detalle_opciones_item_menu doim \
										ON oim.id = doim.id_opciones_item_menu \
								 WHERE imoim.id_item_menu = %s",(idItemMenu,))
				opcionesItemMenu = cursor.fetchall()
				
				detallesOpcionItem = []
				opcionesItem = []
				for indexOpcion, opcion in enumerate(opcionesItemMenu):
					id, nombreOpcion, nombreDetalle, precioDetalle, nroDetalle = opcion
					detallesOpcionItem.append(DetalleOpcionItem(nro_detalle=nroDetalle, nombre=nombreDetalle, precio=precioDetalle)._asdict())
					if indexOpcion + 1 == len(opcionesItemMenu) or id != opcionesItemMenu[indexOpcion + 1][0]:
						opcionesItem.append(OpcionItem(id_opcion=id, nombre=nombreOpcion, detalle=detallesOpcionItem)._asdict())
						detallesOpcionItem = []

				items.append(Item(id=idItemMenu, name=nombreItemMenu, 
					description=descriptionItemMenu, image_url=imageUrlItemMenu, 
					price=float(precioItemMenu), rating=ratingItemMenu, opciones=opcionesItem)._asdict())

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
			cursor.close()
		except Exception as e:
			msg = "Fallo la consulta de getItemsMenu a la base de datos: {}".format(e)
			logger.error(msg)
			raise exceptions.InternalServerError(5002)
		return menu