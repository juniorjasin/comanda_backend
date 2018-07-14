from repository import repo
from utils.logger import Logger

logger = Logger('registerRepo')


class RegisterRepo(repo.Repo):
    def __init__(self):
        super(RegisterRepo, self).__init__()
        logger.debug("RegisterRepo")
        