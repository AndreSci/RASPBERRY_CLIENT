import sqlite3
import datetime
from models.driver import AboutCar


class SQLClass:

    def __init__(self, db_file='./database/wheels_cam.db'):
        self.conn = sqlite3.connect(db_file)
        self.create_table_cars()

    def create_table_cars(self):
        query = """
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            car_number TEXT,
            datetime_create TIMESTAMP,
            block INTEGER
        );
        """
        self.conn.execute(query)
        self.conn.commit()

        query = """
        CREATE TABLE IF NOT EXISTS statistic (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            car_number TEXT,
            datetime_create TIMESTAMP,
            camera TEXT
        );
        """
        self.conn.execute(query)
        self.conn.commit()


class SQLGuest(SQLClass):
    def add_guest(self, user_id, first_name, last_name, car_number):
        now = datetime.datetime.now()
        now = str(now.strftime("%Y-%m-%d/%H.%M.%S"))
        query = f"""
        INSERT INTO guests
        (user_id, first_name, last_name, car_number, datetime_create, datetime_enter, datetime_leave)
        VALUES
        ({user_id}, '{first_name}', '{last_name}', '{car_number}', '{now}', NULL, NULL)
        """
        self.conn.execute(query)
        self.conn.commit()
        print(f"Guest {first_name} {last_name} added.")

    def get_guests(self):
        query = "SELECT * FROM guests"
        cursor = self.conn.execute(query)
        guests = cursor.fetchall()
        return guests


class SQLResident(SQLClass):

    def add_resident(self, resident):
        pass


class SQLCars(SQLClass):
    async def add_car(self, first_name: str, car_number: str):
        now = datetime.datetime.now()
        now = str(now.strftime("%Y-%m-%d/%H.%M.%S"))
        query = f"""
        INSERT INTO cars
        (first_name, car_number, datetime_create, block)
        VALUES
        ('{first_name}', '{car_number}', '{now}', 0)
        """
        self.conn.execute(query)
        self.conn.commit()

    async def get_cars(self):
        query = "SELECT * FROM cars"
        cursor = self.conn.execute(query)
        guests = cursor.fetchall()

        return guests

    async def get_car_by_number(self, car_number):
        query = f"SELECT * FROM cars WHERE car_number = '{car_number}' AND block = 0"
        cursor = self.conn.execute(query)
        car = cursor.fetchall()

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
