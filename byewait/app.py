from tornado.ioloop import IOLoop
import tornado.web
from repository import repo
from services import service
from handlers import loginHandler
from handlers import registerHandler
from handlers import restaurantesHandler
from handlers import menuHandler
from handlers import pedidoHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/login", loginHandler.LoginHandler),
            (r"/register", registerHandler.RegisterHandler),
            (r"/restaurantes", restaurantesHandler.RestaurantesHandler),
            (r"/([a-zA-Z0-9]+)/menu", menuHandler.MenuHandler),
            (r"/([a-zA-Z0-9]+)/pedido", pedidoHandler.PedidoHandler)
        ]
        tornado.web.Application.__init__(self, handlers)


def main():
    app = Application()
    app.listen(8888)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
