import wiringpi
import time
from enum import Enum


BARRIER_PIN = 3


class GPIO:
    """Класс для работы с GPIO"""

    def __init__(self):
        try:
            wiringpi.wiringPiSetup()
            self.is_init = True
        except Exception as e:
            print(e)
            self.is_init = False
            raise WiringCantInit

    def open_barrier(self, pin=BARRIER_PIN) -> PinOutput:
        """Функция открытия шлагбаума возвращает Ret.SUCCESS, если шлагбаум принял команду,
            возвращает Ret.ERROR, если произошла ошибка выполения и возвращает 
            Ret.WARN, если идет отправка на открытие, а реле уже дала эту команду

        """
        ret = Ret.WARN
        if(self.is_init):
            try:
                if read_pin(pin) == PinOutput.LOW:
                    set_pin_mode(pin, PinOutput.HIGH)
                    time.sleep(5)
                    set_pin_mode(pin, PinOutput.LOW)
                    ret = Ret.SUCCESS
                return ret
            except Exception as e:
                print(e)
                raise UnknownException
        else:
            raise WiringNotInit

    def read_pin(self, pin) -> int:
        """Функция чтения GPIO-пина возвращает либо gpio.HIGH либо gpio.LOW"""
        if(self.is_init):
            try:
                if wiringpi.digitalRead(pin) == 1:
                    return PinOutput.HIGH
                else:
                    return PinOutput.LOW
            except Exception as e:
                print(e)
                raise UnknownException
        else:
            raise WiringNotInit

    def set_pin_mode(self, pin, output:PinOutput):
        """Функция установления значения пину"""
        if(self.is_init):
            try:
                wiringpi.pinMode(pin, output)
            except Exception as e:
                print(e)
                raise UnknownException
        else:
            raise WiringNotInit

    class WiringNotInit(Exception):
        "wiringPi isnt initialized"
        pass

    class WiringCantInit(Exception):
        "wiringPi cant initialized"
        pass
    
    class UnknownException(Exception):
        "Unknown exception in gpio"
        pass
    
    class PinOutput(Enum):
        HIGH = 1
        LOW = 0
 
    class Ret(Enum):
        SUCCESS = 1
        WARN = 2
