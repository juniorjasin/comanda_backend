from repository import loginRepo
import jwt
import datetime
import os
import Crypto.PublicKey.RSA as RSA
from utils.logger import Logger

logger = Logger('loginService')

private_key_file = os.path.join(os.environ['INSTALL_DIR'], 'keys','byewaitKeyy')
with open(private_key_file, 'r') as fd:
    private_key = fd.read()

class LoginService:
    def __init__(self):
        self.repo = loginRepo.LoginRepo()

    def validarUsuario(self, userName, password):
        logger.debug('validarUsuario loginService')
        temp = self.repo.validarUsuario(userName,password)
        
        payload = {'userName': userName, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 1000) }
        token = jwt.encode(payload, private_key, algorithm='RS256').decode('utf-8')
        answer = {
            "user": temp,
            "token": token
        }
        return answer

