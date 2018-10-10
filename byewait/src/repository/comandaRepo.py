from repository import repo
from exceptions import exceptions
from utils.logger import Logger
from repository.pedidoRepo import PedidoRepo
from repository.restaurantesRepo import RestaurantesRepo

logger = Logger('comandaRepo')


class ComandaRepo(repo.Repo):
    def __init__(self):
        super(ComandaRepo, self).__init__()
        logger.debug("comandaRepo")

    # def get_all_unfinished_comandas(self):
    #     return "comandita 1 nada mas"

    def get_all_unfinished_comandas(self):
        logger.debug('get_all_unfinished_comandas: obtener todos los pedidos pendientes o en_proceso')
        pedidos = []
        items = []
        restaurante = ()
        id_restaurante = None
        id_mesa = None

        try:
            cursor = self.cnx.cursor()
            consulta = "SELECT pedidos.id_pedidos, pedidos.id_restaurante, pedidos.id_mesa, pedidos.estado_plato, pedidos.estado \
                          FROM pedidos \
                         WHERE pedidos.estado_plato = 'pendiente' \
                            OR pedidos.estado_plato = 'en_proceso' \
                      ORDER BY pedidos.fecha_hora ASC"
            cursor.execute(consulta)
            rows = cursor.fetchall()
            self.cnx.commit()
            cursor.close()

            if rows is not None and len(rows) > 0:
                for index, row in enumerate(rows):
                    id_pedidos, id_restaurante, id_mesa, estado_plato, estado_cuenta = row
                    items = self.getItemsFromPedido(id_pedidos)
                    pedido = {"id_pedidos":id_pedidos, "items":items, "id_mesa":id_mesa, "estado_plato":estado_plato, "estado_cuenta":estado_cuenta}
                    user = self.getUserFromIdPedido(id_pedidos)
                    pedidos.append({"pedido": pedido, "user": user})
                    
            logger.debug('pedidos pediente:{}'.format( pedidos))

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
            
        return (pedidos, restaurante)

    def getUserFromIdPedido(self, id_pedido):

        user = None
        try:        
            cursor = self.cnx.cursor()
            query = "SELECT usuarios.username, usuarios.nombre, usuarios.apellido, usuarios.email  \
                       FROM pedidos \
                       JOIN usuarios \
                         ON pedidos.id_usuario = usuarios.id_usuario \
                      WHERE pedidos.id_pedidos = %s"
            cursor.execute(query, (id_pedido,))
            row = cursor.fetchone()
            cursor.close()

            username, nombre, apellido, email = row
            user = {"username": username, "nombre": nombre, "apellido": apellido, "email": email}

        except Exception as e:
            msg = "getUserFromIdPedido() - Fallo la consulta de getItem a la base de datos: {}".format(e)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)
        
        return user


    # duda: no deberia consultar tambien el id_restaurante? rta: creo que no porque no es parte de la pk
    def getItemsFromPedido(self, id_pedido):
        items = []
        try:        
            cursor = self.cnx.cursor()
            query = "SELECT item_menu.id_item_menu, item_menu.nombre_item_menu, item_menu.description, item_menu.image_url, item_menu.precio, items_pedido.cantidad, items_pedido.aclaraciones \
                       FROM item_menu \
                       JOIN items_pedido \
                         ON item_menu.id_item_menu = items_pedido.id_item_menu \
                      WHERE items_pedido.id_pedidos = %s"
            cursor.execute(query, (id_pedido,))
            rows = cursor.fetchall()
            cursor.close()

            if rows is not None and len(rows) > 0:

                for index, row in enumerate(rows):
                    id, name, description, image_url, price, cantidad, aclaraciones = row
                    opciones = self.getOpcionesFromPedido(id_pedido, id)
                    item = {"id":id, "name":name, "description":description, "image_url":image_url, "price":price, "cantidad":cantidad, "opciones":opciones, "aclaraciones":aclaraciones}
                    items.append(item)

            logger.debug('items asociados al pedido[{}]:{}'.format(id_pedido, items))

        except Exception as e:
            msg = "getItemsFromPedido() - Fallo la consulta de getItem a la base de datos: {}".format(e)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)
        return items

    '''
    con el id_pedidos
    join con opciones_items_pedido
    y despues obtengo nombre de tabla detalle_opciones_item_menu
    '''
    def getOpcionesFromPedido(self, id_pedido, id_item):
        opciones = []
        try:        
            cursor = self.cnx.cursor()
            query = "SELECT detalle_opciones_item_menu.nombre, detalle_opciones_item_menu.precio \
                       FROM item_menu \
                       JOIN items_pedido \
                         ON item_menu.id_item_menu = items_pedido.id_item_menu \
                       JOIN opciones_items_pedido \
                         ON items_pedido.id_item_menu = opciones_items_pedido.id_item_menu \
                        AND items_pedido.id_pedidos = opciones_items_pedido.id_pedidos \
                       JOIN detalle_opciones_item_menu \
                         ON opciones_items_pedido.id_opciones_item_menu = detalle_opciones_item_menu.id_opciones_item_menu \
                        AND opciones_items_pedido.nro_detalle = detalle_opciones_item_menu.nro_detalle \
                      WHERE items_pedido.id_pedidos = %s \
                        AND item_menu.id_item_menu = %s"
            cursor.execute(query, (id_pedido, id_item))
            rows = cursor.fetchall()
            cursor.close()

            if rows is not None and len(rows) > 0:

                for index, row in enumerate(rows):
                    logger.debug('row????:{}'.format(row))

                    nombre, precio = row
                    opcion = {"nombre":nombre, "precio":precio}
                    opciones.append(opcion)

            logger.debug('items asociados al pedido[{}]:{}'.format(id_pedido, opciones))

        except Exception as e:
            msg = "getItemsFromPedido() - Fallo la consulta de getItem a la base de datos: {}".format(e)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)
        return opciones


    

    def actualizarEstadoPlato(self, pedido, nuevoEstado):
        logger.debug('actualizarEstadoPlato()')
        cursor = self.cnx.cursor()
        try: 
            
            logger.debug('pedido:{}'.format(pedido))
            update = "UPDATE pedidos \
                         SET pedidos.estado_plato = %s \
                       WHERE pedidos.id_pedidos = %s \
                         AND pedidos.estado_plato <> %s ;"
            
            values = (nuevoEstado, pedido, nuevoEstado)
            cursor.execute(update, values)

            self.cnx.commit()
            cursor.close()

        except Exception as e:
            self.cnx.rollback()
            msg = "actualizarEstadoPlato() - Fallo update en la base de datos, se hace rollback(). Error: {}".format(e)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)

        return

