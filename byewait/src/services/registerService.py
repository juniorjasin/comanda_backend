import json
from repository import registerRepo
from utils.logger import Logger
import Crypto.PublicKey.RSA as RSA
import jwt
import os
import datetime

private_key_file = os.path.join(os.environ['INSTALL_DIR'], 'keys','byewaitKeyy')
with open(private_key_file, 'r') as fd:
    private_key = fd.read()

logger = Logger('registerService')

class RegisterService:
    def __init__(self):
        self.repo = registerRepo.RegisterRepo()

    def registrarUsuario(self, userName, password, nombre, apellido, email):
        respuesta = self.repo.registrarUsuario(userName, password, nombre, apellido, email)
        payload = {'userName': userName, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 3) }
        token = jwt.encode(payload, private_key, algorithm='RS256').decode('utf-8')
        return { "user": respuesta, "token": token }