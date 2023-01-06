from abc import ABC, abstractmethod

from db_models import Point, Scan
from db_models.Point import association_table
from utils.create_database import engine


class Parser(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return f"Парсер типа: {self.__class__.__name__}"

    @staticmethod
    def _check_file_extension(file_name, __supported_file_extensions__):
        file_extension = f".{file_name.split('.')[-1]}"
        if file_extension not in __supported_file_extensions__:
            raise TypeError(f"Неправильный для парсера тип файла. " \
                            f"Ожидаются файлы типа: {__supported_file_extensions__}")

    @abstractmethod
    def _parse(self, scan: Scan, file_name: str):
        pass

    @staticmethod
    def __insert_to_db(data, db_engine_connection):
        db_engine_connection.execute(Point.Point.__table__.insert(), data["points"])
        db_engine_connection.execute(association_table.insert(), data["points_scans"])

    def _load_data(self, scan: Scan, file_name: str):
        with engine.connect() as db_engine_connection:
            for data in self._parse(scan, file_name):
                self.__insert_to_db(data, db_engine_connection)
            db_engine_connection.commit()
