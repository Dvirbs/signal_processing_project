import pylab
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def output_signal():
    f = 1000
    w = 2. * np.pi * f
    time_interval = 1000
    t = np.linspace(0, time_interval, 100000)
    y = 6 + 3*np.sin(w * t)
    plt.plot(t, y)
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.title('Output Signal - sin_1000hz ')
    plt.savefig()


def input_signal():
    """
    getting the excel the was change for only two column and 1 header ad return x and voltage value
    :return: tuple that first is x value and second is voltage
    """
    path = r'C:\Google One\University\Third year\Lab_B_1\Signal_Processing\Linear system properties\sin1000 Voltage Vs time -distance 7 cm.csv'
    df = pd.read_csv(path)
    time = np.array(df['time'])
    voltage_value = np.array(df['Voltage'])
    plt.plot(time, voltage_value)
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.title('Input Signal - sin_1000hz ')
    plt.savefig()





import pylab
import numpy as N
f = 10.
w = 2. * N.pi * f
time_interval = 1
fig = pylab.figure()
for i, samples in enumerate((5, 50, 500, 5000)):
    pylab.subplot(2, 2, i+1)
    pylab.title('%i samples'%samples)
    t = N.linspace(0, time_interval, samples)
    y = N.sin(w * t)
    pylab.plot(t, y, '.-')
fig.show()
