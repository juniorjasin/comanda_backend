from repository import menuRepo
from utils.logger import Logger

logger = Logger('menuService')

class MenuService:
    def __init__(self):
        self.repo = menuRepo.MenuRepo()

    def getItemsMenu(self, id):        
        items = self.repo.getItemsMenu(id)
        return items