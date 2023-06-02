import os
import configparser
from misc.consts import GlobalConstsControl


class SettingsIni:

    def __init__(self):
        # general settings
        self.settings_file = configparser.ConfigParser()

    def create_settings(self) -> dict:
        """ Функция получения настройки из файла settings.ini. """

        error_mess = 'Успешная загрузка данных из settings.ini'
        ret_value = dict()
        ret_value["result"] = False

        # проверяем файл settings.ini
        if os.path.isfile("settings.ini"):
            try:
                self.settings_file.read("settings.ini", encoding="utf-8")
                # general settings ----------------------------------------
                GlobalConstsControl.set_server_host(self.settings_file["GENERAL"]["SERVER_HOST"])
                GlobalConstsControl.set_server_port(self.settings_file["GENERAL"]["SERVER_PORT"])

                GlobalConstsControl.set_client_host(self.settings_file["GENERAL"]["CLIENT_HOST"])
                GlobalConstsControl.set_client_port(self.settings_file["GENERAL"]["CLIENT_PORT"])

                ret_value["result"] = True

            except KeyError as ex:
                error_mess = f"Не удалось найти поле в файле settings.ini: {ex}"

            except Exception as ex:
                error_mess = f"Не удалось прочитать файл: {ex}"
        else:
            error_mess = "Файл settings.ini не найден в корне проекта"

        ret_value["desc"] = error_mess

        print(error_mess)
        return ret_value
