import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([0, 3, 2, 4, 2, 1, 5, 8, 1, 8])

x_new = np.linspace(0, max(x), num=len(x) * 10)
y_spline = interp1d(x, y, kind='cubic')

plt.plot(x, y, 'o')
plt.plot(x_new, y_spline(x_new), '-')
plt.legend(['Raw data', 'Lagrange', 'Cubic spline'], loc='best')
plt.show()
