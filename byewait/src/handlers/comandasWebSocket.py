from tornado import websocket
import utils.globalvars
from utils.logger import Logger
from services.itemsService import ItemsService
from decorators.handleException import handleException
from model.conexion import Conexion
import json

logger = Logger('---------------comandasWebSocket---------------')

class ComandasWebSocket(websocket.WebSocketHandler):
  def check_origin(self, origin):
    logger.debug('check_origin:{}'.format(origin))
    return True

  @handleException
  def open(self):
    logger.debug('open with conn: {}'.format(self))

  def reportMesaPideCuenta(self, idRestaurante, idMesa):
    logger.debug('reportMesaPideCuenta con idRestaurante: {0}, y con idMesa{1}'.format(idRestaurante, idMesa))
    for conexion in utils.globalvars.webSockConns:
      if conexion.id_restaurante == idRestaurante and conexion.conexion == self:
        conexion.conexion.write_message({'code': 1, 'pedido_cuenta': { 'id_mesa': idMesa }})

  def on_message(self, data):
    logger.debug('on_message con data: {}'.format(data)) 
    # si esto es cierto, es que fue llamado desde frontend app_comanda
    if 'id_restaurante' in data:
      restaurante = json.loads(data)
      id = restaurante['id_restaurante']
      
      conn = Conexion(self, id)
      utils.globalvars.webSockConns.append(conn) 
      logger.debug('agrego conexion:{}'.format(conn))
      return
    
    # si pasa hasta aca, fue llamado desde pedidoHandler
    data['code'] = 0
    id_resto = data['restaurante']
    itemsService = ItemsService()
    # Los items vienen con id nomás, le agrego info adicional(nombre, precio...)
    for item in data['data']['items']:
      id, name, description, image_url, price, rating, opciones = itemsService.getItem(item['id'])

      item['name'] = name
      item['description'] = description
      item['image_url'] = image_url
      item['price'] = price
      item['rating'] = rating
      item['opciones'] = opciones

    # buscar en todas las conexiones y mandarsela a la que corresponda
    for i in utils.globalvars.webSockConns:
      logger.debug('todas las conexiones:{}'.format(i))
      logger.debug('vino pedido de restaurant:{}, y estoy revisando conexion con restaurante:{}'.format(id_resto, i.id_restaurante))
      if i.id_restaurante == id_resto and i.conexion == self:
        logger.debug('se envia a restaurante:{}'.format(i.id_restaurante))
        i.conexion.write_message(data)

  @handleException 
  def on_close(self):
    for i in utils.globalvars.webSockConns:
      if i.conexion == self:
        logger.debug('Conexión cerrada para objeto:{}, del restaurante: {}'.format(i.conexion, i.id_restaurante))
        utils.globalvars.webSockConns.remove(i)

    logger.debug('conexiones abiertas:{}'.format(len(utils.globalvars.webSockConns)))
