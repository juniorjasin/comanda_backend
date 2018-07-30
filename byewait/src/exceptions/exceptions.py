import json
import configparser
from utils.logger import Logger
import os

logger = Logger('exceptions')

# DEVELOPER_MESSAGE_KEY = "developer_message"
USER_MESSAGE = 'user_message'
CODE = 'code'

class InfoException (Exception):
    def __init__(self, info):
        self.info = info

        # Setting user message from config file
        try:
            codes = configparser.ConfigParser()
            codes.read(os.environ["INSTALL_DIR"] + '/config/userMessages.cfg')
            self.info[USER_MESSAGE] = codes[str(self.info[CODE])]["user_message"]
        except Exception as e:
            self.info[USER_MESSAGE] = codes["DEFAULT_USER_MESSAGE"]["user_message"]

        logger.debug(self.info)
        super(InfoException, self).__init__(self.info[USER_MESSAGE])

    def information(self):
        return self.info

    def __str__(self):
        return json.dumps(self.info)

class BadRequest(InfoException):
    def __init__(self, code):
        self.info = dict()
        self.info[USER_MESSAGE] = ''
        self.info[CODE] = code

        super(BadRequest, self).__init__(self.info)

class Unauthorized(InfoException):
    def __init__(self, code):
        self.info = dict()
        self.info[USER_MESSAGE] = ''
        self.info[CODE] = code

        super(Unauthorized, self).__init__(self.info)

class NotFound(InfoException):
    def __init__(self, code):
        self.info = dict()
        self.info[USER_MESSAGE] = ''
        self.info[CODE] = code

        super(NotFound, self).__init__(self.info)


class InternalServerError(InfoException):
    def __init__(self, code):
        self.info = dict()
        self.info[USER_MESSAGE] = ''
        self.info[CODE] = code

        super(InternalServerError, self).__init__(self.info)

class ConflictException(InfoException):
    def __init__(self, code):
        self.info = dict()
        self.info[USER_MESSAGE] = ''
        self.info[CODE] = code

        super(ConflictException, self).__init__(self.info)