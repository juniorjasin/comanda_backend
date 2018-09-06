from repository.menuItemScoreRepo import MenuItemScoreRepo
from utils.logger import Logger

logger = Logger('menuItemScoreService')

class MenuItemScoreService:
    def __init__(self):
        self.repo = MenuItemScoreRepo()

    def insertScore(self, id_item_menu, id_usuario, score):
      logger.debug('insertScore')
      logger.debug(id_item_menu)
      logger.debug(id_usuario)
      logger.debug(score)
      result = self.repo.insertScore(id_item_menu, id_usuario, score)
      return result