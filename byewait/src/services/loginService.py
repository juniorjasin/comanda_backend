import json
from repository import loginRepo


class LoginService:
    def __init__(self):
        self.repo = loginRepo.LoginRepo()