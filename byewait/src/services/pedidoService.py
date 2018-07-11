import json
from repository import pedidoRepo


class PedidoService:
    def __init__(self):
        self.repo = pedidoRepo.PedidoRepo()