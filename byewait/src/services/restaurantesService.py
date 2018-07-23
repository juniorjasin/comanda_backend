import json
from repository import restaurantesRepo
from utils.logger import Logger
from collections import namedtuple
from exceptions import  exceptions

logger = Logger('restaurantesService')

class RestaurantesService:
    def __init__(self):
        self.repo = restaurantesRepo.RestaurantesRepo()

    def getAllRestaurants(self):
        logger.debug('getAllRestaurants')
        restaurantes = self.repo.getAllRestaurants()
        jsonRestaurantes = []
        if len(restaurantes) > 0:
            try:
                jsonRestaurantes = [dict(r) for r in restaurantes]

            except Exception as e:
                msg = "No se pudo convertir la lista de restaurantes a json: {}".format(e)
                logger.error(msg)
                raise exceptions.InternalServerError(5001)
                
        return jsonRestaurantes


