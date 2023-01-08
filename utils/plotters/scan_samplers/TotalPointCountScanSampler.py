from classes.db_models import ScanDB
from utils.plotters.scan_samplers.ScanSamplerABC import ScanSamplerABC


class TotalPointCountScanSampler(ScanSamplerABC):

    def __init__(self, total_point_count):
        self.__total_point_count = total_point_count

    def do_sampling(self, scan: ScanDB):
        pass

    @property
    def total_point_count(self):
        return self.__total_point_count

    @total_point_count.setter
    def total_point_count(self, new_count):
        if isinstance(new_count, int):
            self.__total_point_count = new_count
        else:
            raise TypeError(f"Должно быть целое количество точек. "
                            f"Переданно - {type(new_count)}, {new_count}")
