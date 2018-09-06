from tornado import websocket
import utils.globalvars
from utils.logger import Logger
from services.itemsService import ItemsService
from decorators.handleException import handleException

logger = Logger('comandasWebSocket')

class ComandasWebSocket(websocket.WebSocketHandler):
  def check_origin(self, origin):
    logger.debug('check_origin')
    return True

  @handleException
  def open(self):
    logger.debug('open')
    utils.globalvars.webSockConns.append(self) # Guardo conn del cliente

  @handleException
  def on_message(self, data):
    logger.debug('on_message con data: ' + data)
    itemsService = ItemsService()
    # Los items vienen con id nomás, le agrego info adicional(nombre, precio...)
    for item in data['data']['items']:
      id, name, description, image_url, price = itemsService.getItem(item['id'])
      item['name'] = name
      item['description'] = description
      item['image_url'] = image_url
      item['price'] = price
    self.write_message(data)

  @handleException 
  def on_close(self):
    logger.debug('on_close')
    utils.globalvars.webSockConns.remove(self)
