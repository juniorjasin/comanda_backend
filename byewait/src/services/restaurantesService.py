import json
from repository import restaurantesRepo
from utils.logger import Logger
from collections import namedtuple
from exceptions import  exceptions
from tornado import gen

logger = Logger('restaurantesService')

class RestaurantesService:
    def __init__(self):
        self.repo = restaurantesRepo.RestaurantesRepo()

    def getAllRestaurants(self):
        logger.debug('getAllRestaurants')
        restaurantes = self.repo.getAllRestaurants()
        return restaurantes


