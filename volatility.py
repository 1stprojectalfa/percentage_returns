import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import probabilities
import sequences 

def read_data(csv_file):
    data = pd.read_csv(csv_file, usecols = ['Open','Close'])
    return data

def building_frame(data):
    data = read_data(csv_file)
    data['Percentage Return'] = 100*(data['Close']-data['Open'])/data['Open']
    data['Absolute Percentage Return'] = np.abs(data['Percentage Return'])
    absolute_mean = data['Absolute Percentage Return'].mean()
    absolute_std = data['Absolute Percentage Return'].std()
    data['Distance From Absolute Mean'] = data['Absolute Percentage Return'] - absolute_mean
    return data, absolute_mean, absolute_std

def plotting_scatter(x_axis):
    plt.plot(x_axis, marker = 'o', color = 'g')
    plt.show()

def plotting_histogram_distribution(x_axis):
    plt.hist(x_axis, color = 'r')
    plt.show()
