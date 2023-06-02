import sqlite3
import datetime
from models.driver import AboutCar


class SQLClass:

    def __init__(self, db_file='./database/wheels_cam.db'):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row
        self.create_table_cars()

    def create_table_cars(self):

        # Создаем таблицу cars куда записываются номера
        query = """
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_number TEXT,
            datetime_create TIMESTAMP,
            block INTEGER
        );
        """
        self.conn.execute(query)
        self.conn.commit()

        # Создаем таблицу statistic для записей проездов
        query = """
        CREATE TABLE IF NOT EXISTS statistic (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_number INTEGER,
            datetime_create TIMESTAMP,
            camera INT
        );
        """
        self.conn.execute(query)
        self.conn.commit()

        # Создаем таблицу cameras для индексации
        query = """
        CREATE TABLE IF NOT EXISTS cameras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            camera TEXT
        );
        """
        self.conn.execute(query)
        self.conn.commit()


class SQLCars(SQLClass):
    async def add_car(self, car_number: str):
        """ Добавляет новый номер в БД.
        Возможные ответы: SUCCESS если добавлен номер или есть и не заблокирован.
        BLOCK если номер есть, но заблокирован."""

        query = f"SELECT * FROM cars WHERE car_number = '{car_number}'"
        cursor = self.conn.execute(query)
        car = cursor.fetchone()

        print(len(car))

        car = dict(car)
        if not car:
            now = datetime.datetime.now()
            now = str(now.strftime("%Y-%m-%d/%H.%M.%S"))
            query = f"""
            INSERT INTO cars
            (car_number, datetime_create, block)
            VALUES
            ('{car_number}', '{now}', 0)
            """
            self.conn.execute(query)
            self.conn.commit()

        elif car.get('block') == 1:
            return "BLOCK"
        return "SUCCESS"

    async def camera_in_db(self, camera_name: str) -> int:
        """ Идея такая что если есть камера возвращает id,
        если нет то автоматически добавляет камеру и так же возвращает её id"""

        query = f"SELECT id FROM cameras WHERE camera = '{camera_name}"
        cursor = self.conn.execute(query)
        camera = cursor.fetchone()

        camera = dict(camera)

        if not camera:
            query = f"""
                    INSERT INTO cameras
                    (camera)
                    VALUES
                    ('{camera_name}')
                    """
            self.conn.execute(query)
            self.conn.commit()

            # Дублирование во избежание рекурсии
            query = f"SELECT id FROM cameras WHERE camera = '{camera_name}"
            cursor = self.conn.execute(query)
            camera = cursor.fetchone()

        return camera.get('id')

    async def add_statistic(self, car_number_id: int, camera_name: str):
        """ Принимает id номера (int), имя камеры (str) и создает запись в БД """

        camera_id = self.camera_in_db(camera_name)

        now = datetime.datetime.now()
        now = str(now.strftime("%Y-%m-%d/%H.%M.%S"))
        query = f"""
        INSERT INTO statistic
        (car_number, datetime_create, camera)
        VALUES
        ({car_number_id}, '{now}', {camera_id})
        """
        self.conn.execute(query)
        self.conn.commit()

    async def get_cars(self):
        query = "SELECT * FROM cars"
        cursor = self.conn.execute(query)
        cars = cursor.fetchall()

        return cars

    async def get_car_by_number(self, car_number):
        query = f"SELECT * FROM cars WHERE car_number = '{car_number}' AND block = 0"
        cursor = self.conn.execute(query)
        car = cursor.fetchone()

        return car

    async def delete_car_by_number(self, car_number) -> int:
        query = f"DELETE FROM cars WHERE car_number = '{car_number}'"
        cursor = self.conn.execute(query)
        self.conn.commit()
        res = cursor.rowcount

        print(f"delete_car_by_number.ROWCOUNT = {res}")
        return res

    async def block_unblock_car_by_number(self, car_number, value: int) -> int:
        block_val = 0

        if value == 0:
            block_val = 1

        query = f"UPDATE cars SET (block) = {value} WHERE car_number = '{car_number}' AND block = {block_val}"
        cursor = self.conn.execute(query)
        self.conn.commit()
        res = cursor.rowcount

        print(f"update_car_by_number.ROWCOUNT = {res}")
        return res
