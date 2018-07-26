from tornado.ioloop import IOLoop
import tornado.web
import logging
from services.registerService import RegisterService
from utils.logger import Logger
from handlers import base
from decorators.handleException import handleException

logger = Logger('registerHandler')


class RegisterHandler(base.BaseHandler):

    @tornado.web.asynchronous
    @handleException
    def get(self):
        logger.debug("registerHandler get")
        svc = RegisterService()
        self.finish()

    @tornado.web.asynchronous
    @handleException
    def options(self, restaurante):
        self.finish()
        
    @tornado.web.asynchronous
    @handleException
    def post(self):
        logger.debug("registerHandler post")
        svc = RegisterService()
        self.finish()