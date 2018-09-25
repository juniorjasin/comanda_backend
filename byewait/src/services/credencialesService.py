import os
import jwt
import Crypto.PublicKey.RSA as RSA
import datetime
from utils.logger import Logger
from exceptions import exceptions

logger = Logger('-------------credencialesService--------------')

public_key_file = os.path.join(os.environ['INSTALL_DIR'], 'keys','byewaitKeyy.pub')
with open(public_key_file, 'r') as fd:
    public_key = fd.read()

private_key_file = os.path.join(os.environ['INSTALL_DIR'], 'keys','byewaitKeyy')
with open(private_key_file, 'r') as fd:
    private_key = fd.read()

class CredencialesService:
    def __init__(self):
        pass

    def validarToken(self,token,username):
        logger.debug('validarToken()')
        
        try:
            claims = jwt.decode(token, public_key,algorithms=['RS256'])
            return token
        except jwt.ExpiredSignatureError:
            logger.critical("Token expirado")
            options = {            
            'verify_exp': False,            
            }
            claims = jwt.decode(token, public_key,algorithms=['RS256'], options = options)
            if claims['userName'] != username:
                logger.critical("intento de fraude con token")
                raise exceptions.Unauthorized(2001)    

            logger.debug('expira:{}'.format(datetime.datetime.utcnow() + datetime.timedelta(minutes = 1000)))
            logger.debug('utcnow():{}'.format(datetime.datetime.utcnow()))

            payload = {'userName': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 1000) }
            token = jwt.encode(payload, private_key, algorithm='RS256').decode('utf-8')
            return token
        except jwt.InvalidTokenError:
            logger.critical("Token invalido")
            raise exceptions.Unauthorized(2001)
