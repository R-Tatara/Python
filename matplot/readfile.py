# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


class File:
    def __init__(self, file_name):
        self.input_file = pd.read_csv(file_name, header=0)
        self.header = self.input_file.columns.values.tolist()
        # ----------------------------------------------------
        # A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
        # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        self.x_column = 1  # data of x axis
        self.y_column = 10 # data of y axis
        self.y_column2 = 13 # data of y axis
        # ----------------------------------------------------
        self.x1 = np.array(self.input_file[self.input_file.columns[self.x_column]])
        self.y1 = np.array(self.input_file[self.input_file.columns[self.y_column]])
        self.y2 = np.array(self.input_file[self.input_file.columns[self.y_column2]])
        # plt.xlabel(header[self.x_column])
        # plt.ylabel(header[self.y_column])

    def get_data(self):
        return self.x1, self.y1

    def get_data2(self):
        return self.x1, self.y1, self.y2

