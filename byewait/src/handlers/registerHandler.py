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
        logger.debug("registerHandler get")
        svc = RegisterService()
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self):
        logger.debug("registerHandler post")
        try:
            data = json.loads(self.request.body)
            if 'user' in data and 'username' in data['user'] and 'password' in data['user'] and 'email' in data['user']:
                username = data['user']['username']
                password = data['user']['password']
                try: # Pruebo que se puede encodear en latin-1
                    username.encode('latin-1')
                    password.encode('latin-1')
                except:
                    raise exceptions.BadRequest(3001)
                email = data['user']['email']
                if not bool(re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", email)):
                    raise exceptions.BadRequest(3001)                    
                svc = RegisterService()
                respuesta = svc.registrarUsuario(username, password, email)
                self.write(respuesta)
            else:
                logger.error('Error, el body es incorrecto, faltan atributos')
                raise exceptions.BadRequest(3001)
        except exceptions.BadRequest as ex:
            raise(ex)
        except exceptions.ConflictException as ex:
            raise(ex)
        except exceptions.InternalServerError as ex:
            raise(ex)
        except Exception as ex:
            raise exceptions.InternalServerError(5001)
        self.finish()