from tornado.ioloop import IOLoop
import tornado.web
from repository import repo
from handlers.loginHandler import LoginHandler
from handlers.registerHandler import RegisterHandler
from handlers.restaurantesHandler import RestaurantesHandler
from handlers.menuHandler import MenuHandler
from handlers.pedidoHandler import PedidoHandler
from utils.logger import Logger

logger = Logger('app')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/login/?", LoginHandler),
            (r"/register/?", RegisterHandler),
            (r"/restaurantes/?", RestaurantesHandler),
            (r"/([a-zA-Z0-9]+)/menu/?", MenuHandler),
            (r"/([a-zA-Z0-9]+)/pedido/?", PedidoHandler)
        ]
        tornado.web.Application.__init__(self, handlers)


def main():
    app = Application()
    app.listen(8888)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
