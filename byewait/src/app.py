from tornado.ioloop import IOLoop
import tornado.web
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
from utils.logger import Logger

logger = Logger('app')

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
            (r"/images/(.*)",tornado.web.StaticFileHandler, {"path": "/opt/byewait/images"},),
        ]
        tornado.web.Application.__init__(self, handlers)


def main():
    app = Application()
    app.listen(8888)
    # utils.globals.init() # Inicializo web socket connections en []
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
