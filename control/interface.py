import time
from misc.logger import Logger


class InterfaceRequest:

    def __init__(self, logger: Logger):

        self.logger = logger

    def check_answer(self, json: dict):
        pass
