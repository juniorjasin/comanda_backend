import json
from repository.managerRepository import ManagerRepo
from utils.logger import Logger
from collections import namedtuple
from exceptions import  exceptions
import jwt
import datetime
import os

logger = Logger('itemsService')

private_key_file = os.path.join(os.environ['INSTALL_DIR'], 'keys','byewaitKeyy')
with open(private_key_file, 'r') as fd:
    private_key = fd.read()

class ManagerService:
    def __init__(self):
        self.repo = ManagerRepo()

    def validarUsuario(self, username_ingresado, password_ingresada):
        usuarioCorrecto = self.repo.validarUsuario(username_ingresado, password_ingresada)

        payload = {'userName': usuarioCorrecto['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 1000) }
        token = jwt.encode(payload, private_key, algorithm='RS256').decode('utf-8')
        response = {
            "user": usuarioCorrecto,
            "token":token
        }

        return response