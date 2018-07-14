import json
from repository import registerRepo
from utils.logger import Logger

logger = Logger('registerService')

class RegisterService:
    def __init__(self):
        self.repo = registerRepo.RegisterRepo()