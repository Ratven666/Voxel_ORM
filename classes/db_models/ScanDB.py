from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey

from classes.abc_classes.ScanABC import ScanABC
from config import FILE_NAME

from utils.create_database import Base, Session

from utils.parsers.Parser import Parser
from utils.parsers import TxtParser
from utils.scan_utils.BaseScanIterator import BaseScanIterator

imported_files_table = Table("imported_files", Base.metadata,
                             Column("id", Integer, primary_key=True),
                             Column("file_name", String, nullable=False),
                             Column("scan_id", Integer, ForeignKey("scans.id"))
                             )


class ScanDB(ScanABC, Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    len = Column(Integer)
    min_X = Column(Float)
    max_X = Column(Float)
    min_Y = Column(Float)
    max_Y = Column(Float)
    min_Z = Column(Float)
    max_Z = Column(Float)

    def __init__(self, name):
        super().__init__(name)
        self.__init_scan()
        self.__parser: Parser = TxtParser()

    def __iter__(self):
        return iter(BaseScanIterator(self))

    def load_scan_from_file(self, file_name=FILE_NAME):
        self.__parser.load_data(self, file_name)

    def __init_scan(self):
        def copy_scan_data(self, scan):
            self.id = scan.id
            self.name = scan.name
            self.len = scan.len
            self.min_X, self.max_X = scan.min_X, scan.max_X
            self.min_Y, self.max_Y = scan.min_Y, scan.max_Y
            self.min_Z, self.max_Z = scan.min_Z, scan.max_Z

        with Session() as session:
            scan = session.query(ScanDB).filter(ScanDB.name == self.name).first()
            if scan is not None:
                copy_scan_data(self, scan)
            else:
                session.add(self)
                session.commit()
                scan = session.query(ScanDB).filter(ScanDB.name == self.name).first()
                copy_scan_data(self, scan)

    @property
    def parser(self):
        return self.__parser

    @parser.setter
    def parser(self, parser: Parser):
        if isinstance(parser, Parser):
            self.__parser = parser
        else:
            raise TypeError("Нужно передать объект парсера!")

