import json
from repository import menuRepo


class MenuService:
    def __init__(self):
        self.repo = menuRepo.MenuRepo()