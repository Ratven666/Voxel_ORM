import matplotlib.pyplot as plt

from classes.db_models import ScanDB
from utils.plotters.Plotter import Plotter


class ScanPlotterMPL(Plotter):

    def __init__(self, scan: ScanDB, sampler):
        self.fig = plt.figure()
        self.__ax = self.fig.add_subplot(projection="3d")
        self.__scan = scan
        self.__sampler = sampler

    def __calk_plot_limits(self):
        min_x, min_y, min_z = self.__scan.min_X, self.__scan.min_Y, self.__scan.min_Z
        max_x, max_y, max_z = self.__scan.max_X, self.__scan.max_Y, self.__scan.max_Z
        limits = [max_x - min_x,
                  max_y - min_y,
                  max_z - min_z]
        length = max(limits) / 2
        x_lim = [((min_x + max_x) / 2) - length, ((min_x + max_x) / 2) + length]
        y_lim = [((min_y + max_y) / 2) - length, ((min_y + max_y) / 2) + length]
        z_lim = [((min_z + max_z) / 2) - length, ((min_z + max_z) / 2) + length]
        return {"X_lim": x_lim, "Y_lim": y_lim, "Z_lim": z_lim}

    def __set_plot_limits(self, plot_limits):
        self.__ax.set_xlim(*plot_limits["X_lim"])
        self.__ax.set_ylim(*plot_limits["Y_lim"])
        self.__ax.set_zlim(*plot_limits["Z_lim"])

    def plot(self):
        plt.show()
