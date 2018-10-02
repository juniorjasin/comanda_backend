from repository import repo
from exceptions import exceptions
from utils.logger import Logger
from repository.restaurantesRepo import RestaurantesRepo

logger = Logger('pedidoRepo')


class PedidoRepo(repo.Repo):
    def __init__(self):
        super(PedidoRepo, self).__init__()
        logger.debug("pedidoRepo")

    def insertNewOrder(self, id_restaurante, items, id_usuario, id_mesa):

        logger.debug('insertNewOrder')        
        order = {}

        try:        
            cursor = self.cnx.cursor()
            # inserto el pedido
            insertPedido = 'INSERT INTO pedidos(id_usuario, id_mesa, id_restaurante) VALUES(%s,%s,%s)'
            pedidoUsuario = (id_usuario, id_mesa, id_restaurante)
            cursor.execute(insertPedido, pedidoUsuario)
            idPedido = cursor.lastrowid

            try:
                logger.debug('items:{}'.format(items))
                for item in items:
                    insertItemPedido = 'INSERT INTO items_pedido(id_item_menu, id_pedidos, id_restaurante, cantidad, aclaraciones) VALUES(%s, %s, %s, %s, %s)'
                    items_pedido = ( item['id'], idPedido, id_restaurante, item['cantidad'], item['aclaraciones'] ) 
                    cursor.execute(insertItemPedido, items_pedido)
                    for opcion in item['opciones']:
                        insertOpcion = 'INSERT INTO opciones_items_pedido(id_item_menu, id_pedidos, id_opciones_item_menu, nro_detalle) VALUES(%s, %s, %s, %s)'
                        cursor.execute(insertOpcion, (item['id'], idPedido, opcion['id_opcion'], opcion['nro_detalle']))
            except Exception as e:
                msg = "Fallo insert a items_pedido: {}".format(e)
                logger.error(msg)
                self.cnx.rollback()
                raise exceptions.InternalServerError(5001)

            self.cnx.commit()
            cursor.close()
            
        except Exception as e2:
            msg = "Fallo insert a pedidos: {}".format(e2)
            logger.error(msg)
            raise exceptions.InternalServerError(5002)

        return {"id":idPedido}

    def isValidUserId(self, id):
        return True
        

    def getPedidosPendientes(self, userId):
        logger.debug('---------user:{} quiere obtener sus pedidos------------'.format(userId))
        pedidos = []
        items = []
        restaurante = ()
        id_restaurante = None
        id_mesa = None

        try:
            cursor = self.cnx.cursor()
            consulta = "SELECT pedidos.id_pedidos, pedidos.id_restaurante, pedidos.id_mesa \
                          FROM pedidos\
                         WHERE pedidos.id_usuario = %s \
                           AND pedidos.estado = 'pendiente' \
                      ORDER BY pedidos.fecha_hora ASC"
            cursor.execute(consulta,(userId,))
            rows = cursor.fetchall()
            self.cnx.commit()
            cursor.close()

            if rows is not None and len(rows) > 0:
                for index, row in enumerate(rows):
                    id_pedidos, id_restaurante, id_mesa = row
                    items = self.getItemsFromPedido(id_pedidos)
                    pedidos.append({"id_pedidos":id_pedidos, "nroPedido":index, "items":items})
                    
            logger.debug('pedidos pediente de user[{}]:{}'.format(userId, pedidos))

        except Exception as e:
            messg = "getPedidosPendientes() - Fallo la consulta a la base de datos: {}".format(e)
            logger.error(messg)
            raise exceptions.InternalServerError(5001)

        
        if len(pedidos) > 0 and id_restaurante is not None:
            logger.debug('llamo a getRestaurantById({})'.format(id_restaurante))
            restaurantRepo = RestaurantesRepo()
            restaurante = restaurantRepo.getRestaurantById(id_restaurante)
            restaurante = restaurante._asdict()
            logger.debug('restaurante:{}'.format(restaurante))
            
        return (pedidos, id_mesa, restaurante)

    
    def getItemsFromPedido(self, id_pedido):
        items = []
        try:        
            cursor = self.cnx.cursor()
            query = "SELECT item_menu.id_item_menu, item_menu.nombre_item_menu, item_menu.description, item_menu.image_url, item_menu.precio, items_pedido.cantidad \
                       FROM item_menu \
                       JOIN items_pedido \
                         ON item_menu.id_item_menu = items_pedido.id_item_menu \
                      WHERE items_pedido.id_pedidos = %s"
            cursor.execute(query, (id_pedido,))
            rows = cursor.fetchall()
            cursor.close()

            if rows is not None and len(rows) > 0:

                for index, row in enumerate(rows):
                    id, name, description, image_url, price, cantidad = row
                    item = {"id": id, "name": name, "description":description, "image_url":image_url, "price":price, "cantidad":cantidad}
                    items.append(item)

            logger.debug('items asociados al pedido[{}]:{}'.format(id_pedido, items))

        except Exception as e:
            msg = "getItemsFromPedido() - Fallo la consulta de getItem a la base de datos: {}".format(e)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)
        return items
    


    def actualizarPedidos(self, pedidos, estado):
        logger.debug('actualizarPedidos()')
        cursor = self.cnx.cursor()
        try: 
            for pedido in pedidos:
                logger.debug('pedido:{}'.format(pedido))
                update = "UPDATE pedidos \
                             SET pedidos.estado = %s \
                           WHERE pedidos.id_pedidos = %s \
                             AND pedidos.estado <> %s ;"
                
                values = (estado, pedido['idPedido'], estado)
                cursor.execute(update, values)

            self.cnx.commit()
            cursor.close()

        except Exception as e:
            self.cnx.rollback()
            msg = "actualizarPedidos() - Fallo update en la base de datos, se hace rollback(). Error: {}".format(e)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)

        return