import os
import jwt
import Crypto.PublicKey.RSA as RSA
import datetime
from utils.logger import Logger
from exceptions import exceptions

logger = Logger('credencialesService')

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
        try:
            claims = jwt.decode(token, public_key,algorithms=['RS256'])            
            return token
        except jwt.ExpiredSignatureError:
            logger.critical("Token expirado")
            payload = {'userName': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 3) }
            token = jwt.encode(payload, private_key, algorithm='RS256').decode('utf-8')
            return token
        except jwt.InvalidTokenError:
            logger.critical("Token invalido")
            raise exceptions.Unauthorized(2001)
