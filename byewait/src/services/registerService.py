import json
from repository import registerRepo
from utils.logger import Logger
import Crypto.PublicKey.RSA as RSA
import python_jwt as jwt
import os
import datetime

private_key_file = os.path.join(os.environ['INSTALL_DIR'], 'keys','byewaitKeyy')
with open(private_key_file, 'r') as fd:
    private_key = RSA.importKey(fd.read())

logger = Logger('registerService')

class RegisterService:
    def __init__(self):
        self.repo = registerRepo.RegisterRepo()

    def registrarUsuario(self,userName,password,email):
        respuesta = self.repo.registrarUsuario(userName, password, email)
        payload = {'userName': userName }
        token = jwt.generate_jwt(payload, private_key, 'RS256', datetime.timedelta(minutes=9000))
        return { "user": respuesta, "token": token }