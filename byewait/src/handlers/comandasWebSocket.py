from tornado import websocket
import utils.globalvars
from utils.logger import Logger
from services.itemsService import ItemsService
from model.conexion import Conexion
import json

logger = Logger('------------- comandasWebSocket -------------')

class ComandasWebSocket(websocket.WebSocketHandler):
	def check_origin(self, origin):
		logger.debug('origen:{}'.format(origin))
		return True

	def open(self):
		# conn = Conexion(self, None)
		# utils.globalvars.webSockConns.append(conn) # Guardo con del cliente
		logger.debug('Nueva conexión:{}'.format(self))	

	def on_message(self, data):
		logger.debug('on_message self:{}'.format(self))	

		# si esto es cierto, es que fue llamado desde frontend app_comanda
		if 'id_restaurante' in data:
			restaurante = json.loads(data)
			id = restaurante['id_restaurante']
			logger.debug('message de restaurante:{}'.format(restaurante['id_restaurante']))
			
			conn = Conexion(self, id)
			utils.globalvars.webSockConns.append(conn) 
			logger.debug('agrego conexion:{}'.format(utils.globalvars.webSockConns[-1]))

			return
			
		
		# si pasa hasta aca, fue llamado desde pedidoHandler

		id_resto = data['restaurante']

		itemsService = ItemsService()
		# Los items vienen con id nomás, le agrego info adicional(nombre, precio...)
		for item in data['data']['items']:
			id, name, description, image_url, price, rating = itemsService.getItem(item['id'])
			item['name'] = name
			item['description'] = description
			item['image_url'] = image_url
			item['price'] = price
			item['rating'] = rating

		logger.debug('Nuevo mensaje')
		logger.debug(data)

		# buscar en todas las conexiones y mandarsela a la que corresponda
		
		for i in utils.globalvars.webSockConns:
			logger.debug('todas las conexiones:{}'.format(i))
			logger.debug('vino pedido de restaurant:{}, y estoy revisando conexion con restaurante:{}'.format(id_resto, i.id_restaurante))
			if i.id_restaurante == id_resto and i.conexion == self:
				logger.debug('se envia a restaurante:{}'.format(i.id_restaurante))
				i.conexion.write_message(data)
		

	def on_close(self):
		for i in utils.globalvars.webSockConns:
			if i.conexion == self:
				logger.debug('Conexión cerrada para objeto:{}, del restaurante: {}'.format(i.conexion, i.id_restaurante))
				utils.globalvars.webSockConns.remove(i)

		logger.debug('conexiones abiertas:{}'.format(len(utils.globalvars.webSockConns)))
