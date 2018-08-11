import json
from repository.itemsRepo import ItemsRepo
from utils.logger import Logger
from collections import namedtuple
from exceptions import  exceptions

logger = Logger('itemsService')

class ItemsService:
    def __init__(self):
        self.repo = ItemsRepo()

    def getItem(self, id):
        logger.debug('getItem')
        item = self.repo.getItem(id)
        return item

    def getAll(self):
        # TODO
        pass