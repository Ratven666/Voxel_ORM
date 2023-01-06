from utils.create_database import engine
from config import FILE_NAME

from db_models import PointDB


class TxtParser:

    def __init__(self, file_name=FILE_NAME, chunk_count=100_000, db_engine=engine):
        self.__file_name = file_name
        self.__chunk_count = chunk_count
        self.__engine = db_engine

    # def load_data(self):
    #     with open(self.__file_name, "rt", encoding="utf-8") as file:
    #         points = []
    #         with self.__engine.connect() as db_engine:
    #             for line in file:
    #                 line = line.strip().split()
    #                 point = {"X": line[0], "Y": line[1], "Z": line[2],
    #                          "R": line[3], "G": line[4], "B": line[5]}
    #                 points.append(point)
    #                 if len(points) == self.__chunk_count:
    #                     db_engine.execute(
    #                         PointDB.__table__.insert(),
    #                         points
    #                     )
    #                     points = []
    #             db_engine.execute(
    #                 PointDB.__table__.insert(),
    #                 points
    #             )
    #             db_engine.commit()

    def __parse(self):
        with open(self.__file_name, "rt", encoding="utf-8") as file:
            points = []
            for line in file:
                line = line.strip().split()
                point = {"X": line[0], "Y": line[1], "Z": line[2],
                         "R": line[3], "G": line[4], "B": line[5],
                         "nX": line[6], "nY": line[7], "nZ": line[8]}
                points.append(point)
                if len(points) == self.__chunk_count:
                    yield points
                    points = []
            yield points

    @staticmethod
    def __insert_to_db(data, db_engine_connection):
        db_engine_connection.execute(PointDB.__table__.insert(), data)

    def load_data(self):
        with self.__engine.connect() as db_engine_connection:
            for data in self.__parse():
                self.__insert_to_db(data, db_engine_connection)
            db_engine_connection.commit()
