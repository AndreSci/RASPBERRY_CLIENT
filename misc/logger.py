import threading
import os
import datetime
import inspect

# Данные для logger
LOGGER_PATH = os.path.join(os.getcwd(), "logs\\")


class BColors:
    """ Класс вариантов цвета для текста в консоли """
    col_header = '\033[95m'
    col_okblue = '\033[94m'
    col_okcyan = '\033[96m'
    col_okgreen = '\033[92m'
    col_warning = '\033[93m'
    col_fail = '\033[91m'
    col_endc = '\033[0m'
    col_bold = '\033[1m'
    col_underline = '\033[4m'


def test_dir(log_path) -> bool:
    ret_value = True

    try:
        if not os.path.exists(log_path):  # Если нет директории log_path пробуем её создать.
            os.makedirs(log_path)
            print(f"{BColors.col_warning}Была создана директория для лог-фалов:{BColors.col_endc} {log_path}")
    except Exception as ex:
        print(f"Ошибка при проверка/создании директории лог файлов: {ex}")
        ret_value = False

    return ret_value


class Logger:
    """ Класс вывода данных в консоль и запись в файл """
    def __init__(self):
        self.font_color = False
        self.log_guard = threading.Lock()

    def add_log(self, text: str, print_it=True):
        """ Обшивает текст датой, табуляцией и переходом на новую строку"""
        ret_value = False
        today = datetime.datetime.today()

        for_file_name = str(today.strftime("%Y-%m-%d"))

        date_time = str(today.strftime("%Y-%m-%d/%H.%M.%S"))
        # Создаем лог
        mess = date_time + "\t" + text + "\n"

        if test_dir(LOGGER_PATH):

            # if LOGGER_PATH[-1] == '\\' or LOGGER_PATH[-1] == '/':
            #     pass  # Захотелось использовать pass
            # else:
            #     log_path = LOGGER_PATH + '/'

            with self.log_guard:  # Защищаем поток

                # if print_it:
                #     print(date_time + "\t" + text)
                if print_it:
                    if 'ERROR' == text[:5]:
                        print(f"{BColors.col_fail}{date_time}\t{text}{BColors.col_endc}")
                    elif 'WARNING' == text[:7]:
                        print(f"{BColors.col_warning}{date_time}\t{text}{BColors.col_endc}")
                    else:
                        print(date_time + "\t" + text)

                # Открываем и записываем логи в файл отчета.
                with open(f'{LOGGER_PATH}{for_file_name}.log', 'a', encoding='utf-8') as file:
                    file.write(mess)
                    ret_value = True

        return ret_value

    def event(self, text: str, print_it=True):
        # возьми текущий фрейм объект (frame object)
        current_frame = inspect.currentframe()

        # получи фрейм объект, который его вызвал
        caller_frame = current_frame.f_back

        # возьми у вызвавшего фрейма исполняемый в нём объект типа "код" (code object)
        code_obj = caller_frame.f_code

        # и получи его имя
        code_obj_name = code_obj.co_name

        return self.add_log(f"EVENT\t{code_obj_name}\t{text}", print_it)

    def exception(self, text: str, print_it=True):
        # возьми текущий фрейм объект (frame object)
        current_frame = inspect.currentframe()

        # получи фрейм объект, который его вызвал
        caller_frame = current_frame.f_back

        # возьми у вызвавшего фрейма исполняемый в нём объект типа "код" (code object)
        code_obj = caller_frame.f_code

        # и получи его имя
        code_obj_name = code_obj.co_name

        return self.add_log(f"EXCEPTION\t{code_obj_name}\t{text}", print_it)
