import json
from repository import restaurantesRepo


class RestaurantesService:
    def __init__(self):
        self.repo = restaurantesRepo.RestaurantesRepo()