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
            insertPedido = 'INSERT INTO pedidos(id_usuario, id_mesa) VALUES(%s,%s)'
            pedidoUsuario = (id_usuario, id_mesa)
            cursor.execute(insertPedido, pedidoUsuario)
            idPedido = cursor.lastrowid

            try:
                logger.debug('items:{}'.format(items))
                for item in items:
                    insertItemPedido = 'INSERT INTO items_pedido(id_item_menu, id_pedidos, cantidad, aclaraciones) VALUES(%s, %s, %s, %s)'
                    items_pedido = ( item['id'], idPedido, item['cantidad'], item['aclaraciones'] ) 
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
        