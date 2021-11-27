import numpy as np
# curve-fit() function imported from scipy
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import pandas as pd


def saving_data(sheet_name):
    """
    getting the excel the was change for only two column and 1 header ad return x and voltage value
    :param sheet_name: the name of the sheet
    :return: tuple that first is x value and second is voltage
    """
    path = 'C:/Google One/University/Third year/Lab_B_1/Signal_Processing/fft_project/Intencety/sin_sensetive_1000hz.xlsx'
    df = pd.read_excel(path, sheet_name=sheet_name)
    x_value = np.array(df.iloc[:, 0:1])
    voltage_value = np.array(df.iloc[:, 1:2])

    return x_value, voltage_value


def sheets_name():
    """
    getting all the shit names from the excel file
    :return: a tuple with the sheets name from the close to the far.
    """
    path = 'C:/Google One/University/Third year/Lab_B_1/Signal_Processing/fft_project/Intencety/sin_sensetive_1000hz.xlsx'
    xls = pd.ExcelFile(path)
    list_sheets_name = list()
    for sheet_name in xls.sheet_names:
        list_sheets_name.append(sheet_name)
    list_sheets_name.reverse()
    tuple_sheets_names = tuple(list_sheets_name)
    return tuple_sheets_names


def distance(sheet_name):
    """
    getting a string of the sheet name and return the distance in the string
    :return: distance
    """
    if len(sheet_name) == 30:
        dis = float(sheet_name[-4:-3])
        return dis
    elif len(sheet_name) == 31:
        dis = float(sheet_name[-5:-3])
        return dis


def tests_distance():
    for name in sheets_name():
        typo = type(distance(name))
        if type(distance(name)) != float:
            return False


def max_voltage_list():
    sheets_names = sheets_name()
    voltage_maxi_lst = []
    dis = []
    for sheet in sheets_names:
        voltage_list = saving_data(sheet)[1]
        voltage_maxi_lst.append(max(voltage_list))
        dis.append(distance(sheet))
        'Voltage Vs time -distance 7 cm'
    return dis, voltage_maxi_lst


def plot():
    # x axis values
    x = max_voltage_list()[0]
    # corresponding y axis values
    y = max_voltage_list()[1]
    plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=8)
    plt.xlabel('Distance - axis')
    plt.ylabel('Voltage - axis')
    plt.title('Intensity vs Distance- sin_1000hz')

    # function to show the plot
    plt.show()

    # saving the graph
#    plt.savefig('Intensity vs Distance- sin_1000hz')


#plot()
