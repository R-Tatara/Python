# -*- coding: utf-8 -*-
import numpy as np
import math
from pylab import *


def createLPF(fc):
    a = [0.0] * 3
    b = [0.0] * 3
    denom = 1 + (2 * np.sqrt(2) * np.pi * fc) + 4 * np.pi**2 * fc**2
    b[0] = (4 * np.pi**2 * fc**2) / denom
    b[1] = (8 * np.pi**2 * fc**2) / denom
    b[2] = (4 * np.pi**2 * fc**2) / denom
    a[0] = 1.0
    a[1] = (8 * np.pi**2 * fc**2 - 2) / denom
    a[2] = (1 - (2 * np.sqrt(2) * np.pi * fc) + 4 * np.pi**2 * fc**2) / denom
    return a, b


def createHPF(fc):
    a = [0.0] * 3
    b = [0.0] * 3
    denom = 1 + (2 * np.sqrt(2) * np.pi * fc) + 4 * np.pi**2 * fc**2
    b[0] = 1.0 / denom
    b[1] = -2.0 / denom
    b[2] = 1.0 / denom
    a[0] = 1.0
    a[1] = (8 * np.pi**2 * fc**2 - 2) / denom
    a[2] = (1 - (2 * np.sqrt(2) * np.pi * fc) + 4 * np.pi**2 * fc**2) / denom
    return a, b


def createBPF(fc1, fc2):
    a = [0.0] * 3
    b = [0.0] * 3
    denom = 1 + 2 * np.pi * (fc2 - fc1) + 4 * np.pi**2 * fc1 * fc2
    b[0] = (2 * np.pi * (fc2 - fc1)) / denom
    b[1] = 0.0
    b[2] = - 2 * np.pi * (fc2 - fc1) / denom
    a[0] = 1.0
    a[1] = (8 * np.pi**2 * fc1 * fc2 - 2) / denom
    a[2] = (1.0 - 2 * np.pi * (fc2 - fc1) + 4 * np.pi**2 * fc1 * fc2) / denom
    return a, b


def createBSF(fc1, fc2):
    a = [0.0] * 3
    b = [0.0] * 3
    denom = 1 + 2 * np.pi * (fc2 - fc1) + 4 * np.pi**2 * fc1 * fc2
    b[0] = (4 * np.pi**2 * fc1 * fc2 + 1) / denom
    b[1] = (8 * np.pi**2 * fc1 * fc2 - 2) / denom
    b[2] = (4 * np.pi**2 * fc1 * fc2 + 1) / denom
    a[0] = 1.0
    a[1] = (8 * np.pi**2 * fc1 * fc2 - 2) / denom
    a[2] = (1 - 2 * np.pi * (fc2 - fc1) + 4 * np.pi**2 * fc1 * fc2) / denom
    return a, b


def iir(x, a, b):
    y = [0.0] * len(x)  # Output value from filter
    q = len(a) - 1
    p = len(b) - 1
    for n in range(len(x)):
        for i in range(0, p + 1):
            if n - i >= 0:
                y[n] += b[i] * x[n - i]
        for j in range(1, q + 1):
            if n - j >= 0:
                y[n] -= a[j] * y[n - j]
    return y


def fft(y_original, fs):
    n = 0
    signal_length_original = len(y_original)

    # Zero-filling
    tmp = signal_length_original
    while 1:
        tmp = tmp / 2
        n = n + 1
        if tmp < 2:
            break

    signal_length = pow(2, n)
    for i in range(signal_length - len(y_original)):
        y_original.append(0)

    x_frequency = np.fft.fftfreq(signal_length, d=1.0/fs)
    y_amplitude_tmp = np.fft.fft(y_original[:signal_length])
    y_amplitude = [np.sqrt(amp.real ** 2 + amp.imag ** 2) / signal_length * 2.0 for amp in y_amplitude_tmp]
    # Frequency spectrum
    plot(x_frequency[:signal_length], y_amplitude[:signal_length], linestyle='-')
    xlim([0, fs/2])
    xlabel("Frequency [Hz]")
    ylabel("Amplitude")
    show()


def filter_fft(fs, a, b):
    filter_amplitude = []
    for frequency_list in range(0, int(fs / 2.0)):
        tmp = float(frequency_list) / fs
        nume = b[0] + b[1] * np.exp(-2j * np.pi * tmp) + b[2] * np.exp(-4j * np.pi * tmp)
        deno = 1 + a[1] * np.exp(-2j * np.pi * tmp) + a[2] * np.exp(-4j * np.pi * tmp)
        amp = nume / deno
        filter_amplitude_tmp = np.sqrt(amp.real ** 2 + amp.imag ** 2)
        filter_amplitude.append(filter_amplitude_tmp)
    plot(range(0, int(fs / 2)), filter_amplitude)
    xlabel("Frequency [Hz]")
    show()


def main():
    fs = 100.0
    ts = 1.0 / fs
    time_s = []
    signal_length = 1024
    for i in range(0, signal_length):
        time_s.append(i * ts)

    # Make trigonometric function
    y_original = []
    for i in range(0, signal_length):
        y_original.append(math.sin(2.0 * np.pi * 20.0 * time_s[i]))

    # Make step function, signal_length=1024
    # for i in range(512, 1024):
    #     y_original[i] = 1

    # Set cutoff frequency
    fc1_digital = 0.3     # 正規化したカットオフ周波数
    fc1_digital = 18     # 正規化したカットオフ周波数
    fc2_digital = 25.0     # 正規化したカットオフ周波数
    fc1_analog = np.tan(fc1_digital * np.pi / fs) / (2 * np.pi)
    fc2_analog = np.tan(fc2_digital * np.pi / fs) / (2 * np.pi)

    # Choose type of filter
    # a, b = createLPF(fc1_analog)
    a, b = createHPF(fc2_analog)
    # a, b = createBPF(fc1_analog, fc2_analog)
    # a, b = createBSF(fc1_analog, fc2_analog)
    y_filtered = iir(y_original, a, b)

    plot(time_s, y_original)
    plot(time_s, y_filtered)
    axis([0, 2, -2.0, 2.0])
    xlabel("Time[s]")
    show()

    # Frequency analysis
    fft(y_original, fs)
    fft(y_filtered, fs)
    filter_fft(fs, a, b)


if __name__ == '__main__':
    main()
