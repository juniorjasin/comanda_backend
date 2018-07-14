import json
from repository import pedidoRepo
from utils.logger import Logger

logger = Logger('pedidoService')

class PedidoService:
    def __init__(self):
        self.repo = pedidoRepo.PedidoRepo()