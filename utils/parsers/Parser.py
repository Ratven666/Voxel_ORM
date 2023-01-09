from abc import ABC, abstractmethod

from classes.db_models import PointDB, ScanDB
from classes.db_models.ImportedFileDB import ImportedFileDB
from classes.db_models.PointDB import points_scans_table
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
    def _parse(self, scan: ScanDB, file_name: str):
        pass

    @staticmethod
    def __insert_to_db(data, db_engine_connection):
        db_engine_connection.execute(PointDB.PointDB.__table__.insert(), data["points"])
        db_engine_connection.execute(points_scans_table.insert(), data["points_scans"])

    def load_data(self, scan: ScanDB, file_name: str):
        from utils.scan_utils.Scan_metrics import calc_scan_metrics, update_scan_in_db
        if ImportedFileDB.is_file_already_imported_into_scan(file_name, scan):
            print(f"Файл \"{file_name}\" уже загружен в скан \"{scan.name}\"")
            return
        imp_file = ImportedFileDB(file_name, scan.id)
        with engine.connect() as db_engine_connection:
            for data in self._parse(scan, file_name):
                self.__insert_to_db(data, db_engine_connection)
            db_engine_connection.commit()
        scan_data = calc_scan_metrics(scan)
        update_scan_in_db(scan_data)
        imp_file.insert_in_db()
