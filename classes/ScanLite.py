from classes.abc_classes.PointABC import PointABC
from classes.abc_classes.ScanABC import ScanABC


class ScanLite(ScanABC):

    def __init__(self, name):
        super().__init__(name)
        self.__points = []

    def __iter__(self):
        return iter(self.__points)

    def add_point(self, point):
        if isinstance(point, PointABC):
            self.__points.append(point)
        else:
            raise TypeError(f"Можно добавить только объект точки. "
                             f"Переданно - {type(point)}, {point}")

    @classmethod
    def create_from_another_scan(cls, scan):
        scan_lite = cls(scan.name)
        scan_lite.id = scan.id
        scan_lite.len = scan.len
        scan_lite.min_X, scan_lite.min_Y, scan_lite.min_Z = scan.min_X, scan.min_Y, scan.min_Z
        scan_lite.max_X, scan_lite.max_Y,scan_lite.max_Z = scan.max_X, scan.max_Y, scan.max_Z
        scan_lite.__points = [point for point in scan]
        return scan_lite
