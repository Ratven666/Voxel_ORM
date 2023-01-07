from sqlalchemy import select

from db_models.PointDB import PointDB, points_scans_table

from utils.create_database import engine
from utils.scan_utils.PointLite import PointLite


class BaseScanIterator:

    def __init__(self, scan):
        self.__scan = scan
        self.__engine = engine.connect()
        self.__select = select(PointDB).join(points_scans_table, points_scans_table.c.point_id == PointDB.id)\
                                    .where(self.__scan.id == points_scans_table.c.scan_id)
        self.__query = self.__engine.execute(self.__select)
        self.__iterator = None

    def __iter__(self):
        self.__iterator = iter(self.__query)
        return self

    def __next__(self):
        try:
            row = next(self.__iterator)
            point = PointLite.parse_point_from_db_row(row)
            return point
        except StopIteration:
            self.__engine.close()
            raise StopIteration
        finally:
            self.__engine.close()
