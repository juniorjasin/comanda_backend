from tornado import websocket
import utils.globalvars
from utils.logger import Logger
from services.itemsService import ItemsService

logger = Logger('comandasWebSocket')

class ComandasWebSocket(websocket.WebSocketHandler):
	def check_origin(self, origin):
		return True

	def open(self):
		utils.globalvars.webSockConns.append(self) # Guardo conn del cliente
		logger.debug('Nueva conexión')
	def on_message(self, data):
		itemsService = ItemsService()
		# Los items vienen con id nomás, le agrego info adicional(nombre, precio...)
		for item in data['data']['items']:
			id, name, description, image_url, price = itemsService.getItem(item['id'])
			item['name'] = name
			item['description'] = description
			item['image_url'] = image_url
			item['price'] = price
		logger.debug('Nuevo mensaje')
		logger.debug(data)
		self.write_message(data)

	def on_close(self):
		utils.globalvars.webSockConns.remove(self)
		logger.debug('Conexión cerrada')