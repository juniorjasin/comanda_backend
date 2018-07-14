from repository import repo
from utils.logger import Logger

logger = Logger('menuRepo')


class MenuRepo(repo.Repo):
    def __init__(self):
        super(MenuRepo, self).__init__()
        logger.debug('menuRepo')
        