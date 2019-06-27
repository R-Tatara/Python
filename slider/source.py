# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def main():
    x = np.array([0.0])
    y = np.array([0.0])

    # Graph
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.20)
    plt.xlim([-1.0, 1.0])
    plt.ylim([-1.0, 1.0])
    plt.grid()
    graph, = plt.plot(x[0], y[0])

    def update_x(slider_val):
        x[0] = slider_val
        graph.set_data(x[0], y[0])
        # graph.set_data([0, x[0]], [0, y[0]])

    def update_y(slider_val):
        y[0] = slider_val
        graph.set_data(x[0], y[0])
        # graph.set_data([0, x[0]], [0, y[0]])

    # Position of slider
    slider1_pos = plt.axes([0.1, 0.09, 0.8, 0.03])  # x, y, length, width
    slider2_pos = plt.axes([0.1, 0.05, 0.8, 0.03])  # x, y, length, width

    # Instantiation
    threshold_slider1 = Slider(slider1_pos, 'x', -1, 1, valinit=0)  # min, max
    threshold_slider2 = Slider(slider2_pos, 'y', -1, 1, valinit=0)  # min, max

    # Callback function
    threshold_slider1.on_changed(update_x)
    threshold_slider2.on_changed(update_y)
    fig.canvas.draw_idle()

    # Appearance of the graph
    graph.set_linestyle('-')
    graph.set_linewidth(5)
    graph.set_marker('o')
    graph.set_markerfacecolor('g')
    graph.set_markeredgecolor('g')
    graph.set_markersize(10)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()