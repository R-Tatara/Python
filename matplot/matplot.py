# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
from datetime import datetime

import numpy as np
import math
import readfile


class MatPlot:
    def __init__(self):
        self.number = 1
        self.color_list = {"Red"   :"#e41a1c", \
                           "Blue"  :"#377eb8", \
                           "Green" :"#4daf4a", \
                           "Purple":"#984ea3", \
                           "Orange":"#ff7f00", \
                           "Yellow":"#ffff33", \
                           "Brown" :"#a65628", \
                           "Pink"  :"#f781bf"}

    def set_appearance(self):
        # ----------------------------------------------------
        figsize_hor = 3.14  # Length[inch]
        figsize_ver = 2.355 # Width[inch]
        x_min = 0.0
        x_max = 2.0001
        y_min = -2.0
        y_max = 2.0001
        x_step = 0.5
        y_step = 0.5
        # ----------------------------------------------------
        plt.figure(self.number, figsize=(figsize_hor, figsize_ver))
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.rcParams['mathtext.fontset'] = 'stix'
        plt.rcParams['font.size'] = 8
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['axes.linewidth'] = 0.5
        plt.rcParams['axes.grid'] = True
        plt.rcParams['grid.linestyle'] = '--'
        plt.rcParams['grid.linewidth'] = 0.3
        plt.rcParams["legend.edgecolor"] = 'black'
        plt.rcParams["legend.fancybox"] = False
        plt.xlabel(r"$x$")
        plt.ylabel(r"$y$")
        plt.axis([x_min, x_max, y_min, y_max])
        plt.xticks(np.arange(x_min, x_max, x_step))
        plt.yticks(np.arange(y_min, y_max, y_step))
        plt.tick_params(width = 0.5)
        plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f')) # Display format of x axis
        plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f')) # Display format of y axis
        return

    def make(self, x1, y1):
        self.set_appearance()
        plt.plot(x1, y1, label="1", color=self.color_list["Blue"], linewidth=0.7)
        self.number += 1
        return

    def make2(self, x1, y1, y2):
        self.set_appearance()
        plt.plot(x1, y1, label="1", color=self.color_list["Red"], linewidth=0.7, zorder=2)
        plt.plot(x1, y2, label="2", color=self.color_list["Blue"], linewidth=0.7, zorder=1)
        plt.legend(loc = 'lower right').get_frame().set_linewidth(0.5) # loc = 'upper/lower, left/right/center'
        self.number += 1
        return

    def save_picture(self):
        dt = datetime.now()
        time_str = dt.strftime('%m%d%H%M')
        try:
            os.makedirs("./figure")
        except FileExistsError:
            pass
        plt.savefig("./figure/" + time_str + ".png", dpi=300, bbox_inches="tight")
        return


def main():
    mplot = MatPlot()
    x1 = np.zeros(256)
    y1 = np.zeros(256)
    y2 = np.zeros(256)
    for i in range(256):
        x1[i] = i * 0.01
        y1[i] = math.sin(2 * math.pi * x1[i])
        y2[i] = math.sin(2 * math.pi * x1[i] + 0.5)

    # csv = readfile.File("./figure/data.csv")
    # x1, y1, y2 = csv.get_data2()

    mplot.make2(x1, y1, y2)
    mplot.save_picture()
    plt.show()
    pass


if __name__ == '__main__':
    main()