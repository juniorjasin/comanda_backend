from repository import repo
from utils.logger import Logger

logger = Logger('loginRepo')


class LoginRepo(repo.Repo):
    def __init__(self):
        super(LoginRepo, self).__init__()
        logger.debug("loginRepo")

        