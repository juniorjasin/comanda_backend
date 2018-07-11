import json
from repository import registerRepo


class RegisterService:
    def __init__(self):
        self.repo = registerRepo.RegisterRepo()