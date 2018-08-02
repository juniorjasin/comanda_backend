import tornado.web
import json
from decorators.handleException import handleException
from services.loginService import LoginService
from utils.logger import Logger
from handlers import base
from exceptions import exceptions

logger = Logger('loginHandler')

class LoginHandler(base.BaseHandler):

    @tornado.web.asynchronous
    @handleException
    def get(self):
        logger.debug("loginHandler get")
        svc = LoginService()
        token = svc.validarUsuario()
        self.write(token)
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self):
        logger.debug("loginHandler post")
        try:
            data = json.loads(self.request.body)
            if 'user' in data and 'username' in data['user'] and 'password' in data['user']:
                username = data['user']['username']
                password = data['user']['password']
                try: # Pruebo que se puede encodear en latin-1
                    username.encode('latin-1')
                    password.encode('latin-1')
                except:
                    raise exceptions.BadRequest(3001)
                svc = LoginService()                
                respuesta = svc.validarUsuario(username,password)
                self.write(respuesta)
            else:
                logger.error('Error, el body es incorrecto, faltan atributos')
                raise exceptions.BadRequest(3001)
        except exceptions.BadRequest as ex:
            raise(ex)
        except exceptions.InternalServerError as ex:
            raise(ex)
        except exceptions.NotFound as ex:
            raise(ex)
        except Exception as e:
            msg = "Error: {}".format(e)
            logger.error(msg)
            raise exceptions.BadRequest(4001)
        self.finish()