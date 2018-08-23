from repository.menuItemScoreRepo import MenuItemScoreRepo
from utils.logger import Logger

logger = Logger('menuItemScoreService')

class MenuItemScoreService:
    def __init__(self):
        self.repo = MenuItemScoreRepo()

    def insertScore(self, idItemMenu, idUsuario, score):
      logger.debug('insertScore')
      result = self.repo.insertScore(idItemMenu, idUsuario, score)
      return result