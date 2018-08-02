from functools import wraps
from exceptions import exceptions as exception
from utils.logger import Logger

logger = Logger('checkExceptions')

def handleException(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        try:
            logger.debug('Inside decorator. Calling decorated function')
            return f(*args, **kwds)
        except exception.InfoException as ex:
            handler = args[0]
            # Viene de la excepción
            responseBody = str(ex)
            if isinstance(ex, exception.BadRequest):
                handler.set_status(400)
            elif isinstance(ex, exception.Unauthorized):
                handler.set_status(401)
            elif isinstance(ex, exception.NotFound):
                handler.set_status(404)
            elif isinstance(ex, exception.ConflictException):
                handler.set_status(409)
            elif isinstance(ex, exception.InternalServerError):
                handler.set_status(500)
        except Exception as ex: # Caso de exception que se nos pase, se atrapa acá
            handler = args[0]
            logger.error('Exception no contemplada!!!')
            handler.set_status(500)
            # Hay que cambiar está línea para que no esté hardcodeado, no sé me ocurre
            # una buena forma ahora...
            responseBody = {"user_message": "Error interno del servidor", "code": 4001}
        finally:
            handler.finish(responseBody)
    return wrapper