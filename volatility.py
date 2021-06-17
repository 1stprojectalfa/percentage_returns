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

files = ['AAPL', 'AMD', 'BAC', 'EEM', 'GLD', 'IBM', 'MU', 'NIO', 'SBUX', 'SLV', 'SNAP', 'SPY', 'TLT', 'UBER', 'XOM', 'FXI']

for name in files:
    csv_file = name + '_Week_260.csv'
    print('---------------------------------------------------------------------------------------------------')
    print(csv_file)
    data = read_data(csv_file)
    data, abs_mean, abs_std = building_frame(data)
    print(data)
    print(f'Absolute Mean: {abs_mean}')
    returns = data['Distance From Absolute Mean']
    target = probabilities.building_target_range(returns, 0, abs_mean)
    probabilities.printing_probabilities(returns, target)
    values = list(data['Distance From Absolute Mean'])
    runs = sequences.builiding_sequences(values, 0, np.amax(values))
    sequences.display_sequences(runs)
    periods_duration = sequences.building_lengths_distribution(runs)
    print(periods_duration)