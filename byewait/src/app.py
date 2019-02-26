from tornado.ioloop import IOLoop
import tornado.web
import os
from utils.logger import Logger
from memory_profiler import profile
import sys

logger = Logger('app')

# Crear carpeta para logs
newpath = os.environ['INSTALL_DIR'] + '/logs' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

from handlers.loginHandler import LoginHandler
from handlers.registerHandler import RegisterHandler
from handlers.restaurantesHandler import RestaurantesHandler
from handlers.menuHandler import MenuHandler
from handlers.pedidoHandler import PedidoHandler
from handlers.pedirCuentaHandler import PedirCuentaHandler
from handlers.comandasWebSocket import ComandasWebSocket
from handlers.menuItemScoreHandler import MenuItemScoreHandler
from handlers.managerHandler import ManagerHandler
from handlers.credencialesHandler import CredencialesHandler
from handlers.historialPedidosHandler import HistorialPedidosHandler 
from handlers.comandaHandler import ComandaHandler

class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r"/login/?", LoginHandler),
            (r"/register/?", RegisterHandler),
            (r"/restaurantes/?", RestaurantesHandler),
            (r"/([a-zA-Z0-9]+)/menu/?", MenuHandler),
            (r"/([a-zA-Z0-9]+)/pedido/?", PedidoHandler),
            (r"/([a-zA-Z0-9]+)/cuenta/pedir/?", PedirCuentaHandler),
            (r"/menu/item/score/?", MenuItemScoreHandler),
            (r"/comandas/?", ComandasWebSocket),
            (r"/manager/?", ManagerHandler),
            (r"/credenciales/?", CredencialesHandler),
            (r"/restaurantes/historial/pedidos/?", HistorialPedidosHandler),
            (r"/comandaManager/?", ComandaHandler),
            (r"/images/(.*)",tornado.web.StaticFileHandler, {"path": "/opt/byewait/images"},),
        ]
        tornado.web.Application.__init__(self, handlers)

def main():
    ''' codigo original: menos performante '''
    # app = Application()
    # app.listen(8888)
    # logger.debug("listening at 8888")
    # # utils.globals.init() # Inicializo web socket connections en []
    # IOLoop.instance().start()

    ''' segunda version: usa todos los procesadores, mucho mas performante que el original '''
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)  # forks one process per cpu
    logger.debug("listening at 8888")
    IOLoop.current().start()
    
    ''' tercera version: abre sockets, igual performance  '''
    # app = Application()
    # sockets = tornado.netutil.bind_sockets(8888)
    # tornado.process.fork_processes(0)
    # server = tornado.httpserver.HTTPServer(app)
    # server.add_sockets(sockets)
    # logger.debug("listening at 8888")
    # IOLoop.current().start()


if __name__ == '__main__':
    main()
    
    
