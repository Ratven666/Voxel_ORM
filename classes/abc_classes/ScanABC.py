from utils.plotters.Plotter import Plotter
from utils.plotters.ScanPlotterMPL import ScanPlotterMPL
from utils.scan_utils.scan_samplers.TotalPointCountScanSampler import TotalPointCountScanSampler


class ScanABC:

    def __init__(self, name, id_=None):
        self.id = id_
        self.name: str = name
        self.len: int = 0
        self.min_X, self.max_X = None, None
        self.min_Y, self.max_Y = None, None
        self.min_Z, self.max_Z = None, None

    def __str__(self):
        return f"{self.__class__.__name__} "\
               f"[id: {self.id},\tName: {self.name}\tLEN: {self.len}]"

    def __repr__(self):
        return f"{self.__class__.__name__} [ID: {self.id}]"

    def __len__(self):
        return self.len

    def plot(self, plotter=ScanPlotterMPL()):
        plotter.plot(self)

    # @property
    # def plotter(self, plotter=ScanPlotterMPL()):
    #     return self.__plotter
    #
    # @plotter.setter
    # def plotter(self, plotter: Plotter):
    #     if isinstance(plotter, Plotter):
    #         self.__plotter = plotter
    #     else:
    #         raise TypeError(f"Нужно передать объект плоттера! "
    #                         f"Передан {type(plotter)}, {plotter}")
