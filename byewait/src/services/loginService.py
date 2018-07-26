from repository import loginRepo
import python_jwt as jwt
import datetime
import os
import Crypto.PublicKey.RSA as RSA
from utils.logger import Logger

logger = Logger('loginService')

private_key_file = os.path.join(os.environ['INSTALL_DIR'], 'keys','byewaitKeyy')
with open(private_key_file, 'r') as fd:
    private_key = RSA.importKey(fd.read())

class LoginService:
    def __init__(self):
        self.repo = loginRepo.LoginRepo()

    def validarUsuario(self):
        #asumimos que el usuario existe (hay que hacer la consulta en bd)

        payload = {'userName': 'andy'}
        token = jwt.generate_jwt(payload, private_key, 'RS256', datetime.timedelta(minutes=9000))
        return {"token":token}

