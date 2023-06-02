import os
from misc.logger import Logger

# Режим при котором отображается видео, ведутся дополнительные сообщения и отключено управление барьером
DEBUG_MODE = True

# Приоритетное открытие барьера


# Удалённый сервер
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8091

# Клиент self
CLIENT_HOST = "127.0.0.1"
CLIENT_PORT = 8092

# Полный путь к проекту
PATH = os.getcwd()

# Создаем глобальный объект logger
LOGGER = Logger()


class GlobalConstsControl:

    @staticmethod
    def set_server_host(value: str):
        global SERVER_HOST
        SERVER_HOST = value

    @staticmethod
    def set_server_port(value: int):
        global SERVER_PORT
        SERVER_PORT = int(value)

    @staticmethod
    def set_client_host(value: str):
        global CLIENT_HOST
        CLIENT_HOST = value

    @staticmethod
    def set_client_port(value: int):
        global CLIENT_PORT
        CLIENT_PORT = int(value)

    @staticmethod
    def create_logger():
        """ Пересоздаем объект logger с новыми параметрами из settings.ini """
        global LOGGER
        LOGGER = Logger()

    @staticmethod
    def get_client_host():
        return CLIENT_HOST

    @staticmethod
    def get_client_port():
        return CLIENT_PORT
