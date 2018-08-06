from tornado import websocket
import utils.globalvars
from utils.logger import Logger

logger = Logger('comandas-websocket')

class ComandasWebSocket(websocket.WebSocketHandler):
	def check_origin(self, origin):
		return True

	def open(self):
		utils.globalvars.webSockConns.append(self) # Guardo conn del cliente
		logger.debug('Nueva conexión')

	def on_message(self, message):
		logger.debug('Nuevo mensaje')
		logger.debug(message)
		self.write_message(message)

	def on_close(self):
		utils.globalvars.webSockConns.remove(self)
		logger.debug('Conexión cerrada')