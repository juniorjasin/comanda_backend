from repository import repo
from utils.logger import Logger

logger = Logger('restaurantesRepo')


class RestaurantesRepo(repo.Repo):
    def __init__(self):
        super(RestaurantesRepo, self).__init__()
        logger.debug('restaurantesRepo')
        