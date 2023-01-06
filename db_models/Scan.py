from sqlalchemy import Column, Integer, String

from config import FILE_NAME

from utils.create_database import Base, Session
from utils.parsers.Parser import Parser
from utils.parsers import TxtParser


class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    len = Column(Integer)

    def __init__(self, name):
        self.name: str = name
        self.len: int = 0
        self.__init_scan()
        self.__parser: Parser = TxtParser()

    def __str__(self):
        return f"Scan [id: {self.id},\tName: {self.name}\tLEN: {self.len}]"

    def __repr__(self):
        return f"Scan [ID: {self.id}]"

    def __len__(self):
        return self.len

    @property
    def parser(self):
        return self.__parser

    @parser.setter
    def parser(self, parser: Parser):
        if isinstance(parser, Parser):
            self.__parser = parser
        else:
            raise TypeError("Нужно передать объект парсера!")

    def load_scan_from_file(self, file_name=FILE_NAME):
        self.__parser._load_data(self, file_name)

    def __init_scan(self):
        def copy_scan_data(self, scan):
            self.id = scan.id
            self.name = scan.name
            self.len = scan.len

        with Session() as session:
            scan = session.query(Scan).filter(Scan.name == self.name).first()
            if scan is not None:
                copy_scan_data(self, scan)
            else:
                session.add(self)
                session.commit()
                scan = session.query(Scan).filter(Scan.name == self.name).first()
                copy_scan_data(self, scan)





    def test(self):

        with Session() as s:
            sc = s.query(Scan).get(self.id)
            sc.len += 100
            self.len = sc.len
            print(self, "!!!")

            s.commit()
