from repository import repo
import logging


logger = logging.getLogger('menuRepo')
logger.setLevel(logging.DEBUG)
logger.propagate = False
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class MenuRepo(repo.Repo):
    def __init__(self):
        super(MenuRepo, self).__init__()
        logger.debug('menuRepo')
        