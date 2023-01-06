from db_models import Scan
from utils.create_database import Session
from config import CHUNK_COUNT

from db_models.Point import Point
from utils.parsers.Parser import Parser


class TxtParser(Parser):
    __supported_file_extension__ = [".txt"]

    def __init__(self, chunk_count=CHUNK_COUNT):
        super().__init__()
        self.__chunk_count = chunk_count
        self.__last_point_id = self.__get_last_point_id()

    @property
    def chunk_count(self):
        return self.__chunk_count

    @chunk_count.setter
    def chunk_count(self, chunk_count: int):
        self.__chunk_count = chunk_count

    @staticmethod
    def __get_last_point_id():
        with Session() as session:
            query = session.query(Point).order_by(Point.id.desc()).first()
            if query:
                return query.id
            return 0

    def _parse(self, scan: Scan, file_name: str):
        super()._check_file_extension(file_name, self.__supported_file_extension__)
        with open(file_name, "rt", encoding="utf-8") as file:
            points = []
            points_scans = []
            for line in file:
                line = line.strip().split()
                self.__last_point_id += 1
                point = {"id": self.__last_point_id,
                         "X": line[0], "Y": line[1], "Z": line[2],
                         "R": line[3], "G": line[4], "B": line[5],
                         # "nX": line[6], "nY": line[7], "nZ": line[8],
                         }
                point_scan = {"point_id": self.__last_point_id, "scan_id": scan.id}
                points.append(point)
                points_scans.append(point_scan)
                if len(points) == self.__chunk_count:
                    yield {"points": points, "points_scans": points_scans}
                    points, points_scans = [], []
            yield {"points": points, "points_scans": points_scans}
