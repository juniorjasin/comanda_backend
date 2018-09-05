import json
import os
import jwt
import Crypto.PublicKey.RSA as RSA
from utils.logger import Logger
from exceptions import exceptions

logger = Logger('checkAuthentication')

public_key_file = os.path.join(os.environ['INSTALL_DIR'], 'keys','byewaitKeyy.pub')
with open(public_key_file, 'r') as fd:
    public_key = fd.read()

def checkAuthentication(f):
    def wrapper(*args):
        logger.debug('check_authentication decorator')
        request = args[0].request
        token = request.headers.get("Authorization")
        
        try:
            claims = jwt.decode(token, public_key,algorithms=['RS256'])
            logger.debug(claims)
            logger.debug(claims['userName'])
        except jwt.ExpiredSignatureError:            
            logger.critical("Token expirado")
            raise exceptions.Unauthorized(2001)
        except jwt.InvalidTokenError:
            logger.critical("Token invalido")
            raise exceptions.Unauthorized(2001)
        except Exception as ex:
            logger.debug("Error1: {0}".format(ex))
            raise Exception

        return f(*args)
    return wrapper