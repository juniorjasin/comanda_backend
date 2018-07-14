from repository import repo
from utils.logger import Logger

logger = Logger('pedidoRepo')


class PedidoRepo(repo.Repo):
    def __init__(self):
        super(PedidoRepo, self).__init__()
        logger.debug("pedidoRepo")
        