from tornado.ioloop import IOLoop
import tornado.web
import logging
import json
from services.registerService import RegisterService
from utils.logger import Logger
from handlers import base
from decorators.handleException import handleException
from exceptions import exceptions
import re

logger = Logger('registerHandler')

class RegisterHandler(base.BaseHandler):
  
    @tornado.web.asynchronous
    @handleException
    def get(self):
        logger.debug("get")
        svc = RegisterService()
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self):
        logger.debug("post")
        data = json.loads(self.request.body.decode('utf-8'))
        try:
            username = data['user']['username']
            password = data['user']['password']
            nombre = data['user']['nombre']
            apellido = data['user']['apellido']
            email = data['user']['email']
            username.encode('latin-1')
            password.encode('latin-1')
            nombre.encode('latin-1')
            apellido.encode('latin-1')
        except Exception as e:
            logger.error('Body incorrecto, exception: : {}'.format(e) + ' body: {}'.format(data)) 
            raise exceptions.BadRequest(3001)
        if not bool(re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", email)):
            logger.error('Mal formato de email, email: {}'.format(email))
            raise exceptions.BadRequest(3001)
        svc = RegisterService()
        respuesta = svc.registrarUsuario(username, password, nombre, apellido, email)
        self.write(respuesta)
        self.finish()