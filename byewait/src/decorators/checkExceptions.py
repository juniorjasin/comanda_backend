from functools import wraps
import logging

from exceptions import exceptions as exception

logger = logging.getLogger('checkExceptionsHandler')
logger.setLevel(logging.DEBUG)
logger.propagate = False
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def checkExceptions(f):
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
            elif isinstance(ex, exception.InternalServerError):
                handler.set_status(500)
            handler.finish(responseBody)
    return wrapper