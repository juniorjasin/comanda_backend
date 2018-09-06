import tornado.web
import json
from decorators.handleException import handleException
from exceptions import exceptions
from utils.logger import Logger
from services.credencialesService import CredencialesService
from handlers import base


logger = Logger('credencialesHandler')

class CredencialesHandler(base.BaseHandler):

    @tornado.web.asynchronous
    @handleException
    def options(self):
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def post(self):
        logger.debug("credentialHandler post")
        try:
            data = json.loads(self.request.body)
            token = data["token"]
            username = data["username"]
        except:
            logger.error('Error, el body es incorrecto, faltan atributos')
            raise exceptions.BadRequest(3001)
        
        svc = CredencialesService()
        token = svc.validarToken(token,username)
        self.write({"token":token})
        self.finish()