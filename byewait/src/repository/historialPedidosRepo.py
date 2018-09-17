from repository import repo
from utils.logger import Logger
from exceptions import exceptions
from model.filaHistorialPedidos import FilaHistorialPedidos

logger = Logger('historialPedidosRepo')

class HistorialPedidosRepo(repo.Repo):
    def __init__(self):
        super(HistorialPedidosRepo, self).__init__()
    
    def validarManagerCoincideRestaurante(self, idManager, idRestaurante):        
        logger.debug('validarManagerCoincideRestaurante')
        respuesta = False 
        try:
            cursor = self.cnx.cursor()
            consulta = "SELECT id_restaurante FROM managers WHERE managers.id_manager = %s"
            cursor.execute(consulta,(idManager,))
            row = cursor.fetchone()
            if row is not None and idRestaurante == row[0]:
                respuesta = True
            cursor.close()
        except Exception as e:
            messg = "Fallo la consulta a la base de datos: {}".format(e)
            logger.error(messg)
            raise exceptions.InternalServerError(5001)
        return respuesta

    def getHistorialPedidos(self, idRestaurante):
        logger.debug('getHistorialPedidos')
        respuesta = [] 
        try:
            cursor = self.cnx.cursor()
            cursor.execute("select p.id_pedidos, \
                                   DATE_FORMAT(p.fecha_hora, '%%d-%%m-%%Y') DATEONLY, \
                                   DATE_FORMAT(p.fecha_hora, '%%H:%%i') TIMEONLY, \
                                   sum(im.precio) as monto_total, \
                                   u.nombre, \
                                   u.apellido \
                              from pedidos p \
                                join usuarios u \
                                  on u.id_usuario = p.id_usuario \
                                join items_pedido ip \
                                  on ip.id_pedidos = p.id_pedidos \
                                join item_menu im \
                                  on im.id_item_menu = ip.id_item_menu \
                              where p.id_restaurante = %s \
                              group by p.id_pedidos", (idRestaurante,))
            pedidos = cursor.fetchall()

            cursor.execute("select p.id_pedidos, \
                                   im.nombre_item_menu, \
                                   ip.cantidad, \
                                   im.precio, \
                                   im.image_url \
                            from pedidos p \
                              join items_pedido ip \
                                on p.id_pedidos = ip.id_pedidos \
                              join item_menu im \
                                on ip.id_item_menu = im.id_item_menu \
                            where p.id_restaurante = %s \
                            order by p.id_pedidos", (idRestaurante,))
            itemsPedidos = cursor.fetchall()

            for pedido in pedidos:
                items = [] 
                for item in itemsPedidos:
                    if item[0] == pedido[0]:
                        items.append({
                            'nombre': item[1],
                            'cantidad_pedida': item[2],
                            'precio': item[3],
                            'image_url': item[4]
                        })
                respuesta.append(FilaHistorialPedidos(
                    id = pedido[0],
                    fecha = pedido[1],
                    hora = pedido[2],
                    monto_total = pedido[3],
                    items = items,
                    nombre_usuario = pedido[4],
                    apellido_usuario = pedido[5])._asdict())
            cursor.close()
        except Exception as e:
            messg = "Fallo la consulta a la base de datos: {}".format(e)
            logger.error(messg)
            raise exceptions.InternalServerError(5001)
        return respuesta