from repository import repo
from exceptions import exceptions
from utils.logger import Logger

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
        try:
            cursor = self.cnx.cursor()
            consulta = "SELECT pedidos.id_pedidos, pedidos.id_restaurante, pedidos.id_mesa \
                          FROM pedidos\
                         WHERE pedidos.id_usuario = %s \
                           AND pedidos.estado = 'pendiente'"
            cursor.execute(consulta,(userId,))
            rows = cursor.fetchone()
            self.cnx.commit()
            cursor.close()
            # if rows != None:
                # items = getItemsFromPedido(rows)

            logger.debug('-------------------OBTUVE DE LA DB-------------------')
            logger.debug(rows)

        except Exception as e:
            messg = "Fallo la consulta a la base de datos: {}".format(e)
            logger.error(messg)
            raise exceptions.InternalServerError(5001)

        return pedidos

    def getItemsFromPedido(self, id_pedido):
        pass

    

    