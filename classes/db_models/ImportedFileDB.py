from sqlalchemy import Column, Integer, String, ForeignKey, and_
from sqlalchemy import select

# from classes.db_models.ScanDB import imported_files_table
from utils.create_database import Base, Session, engine


class ImportedFileDB:

    def __init__(self, file_name, scan_id):
        self.file_name = file_name
        self.hash = None
        self.scan_id = scan_id

    @staticmethod
    def is_file_already_imported_into_scan(file_name, scan):
        from classes.db_models.ScanDB import imported_files_table

        select_ = select(imported_files_table).where(and_(imported_files_table.c.file_name == file_name,
                                                          imported_files_table.c.scan_id == scan.id))
        with engine.connect() as e:
            imp_file = e.execute(select_).first()
            print(imp_file)

        if imp_file is None:
            return False
        return True

    def insert_in_db(self):
        with engine.connect() as e:
            from classes.db_models.ScanDB import imported_files_table
            e.execute(imported_files_table.insert(), {"file_name": self.file_name,
                                                      "scan_id": self.scan_id})
            e.commit()
