import numpy as np
import pandas as pd

def read_data(csv_file):
    data = np.array(pd.read_csv(csv_file, usecols = ['Open','Close']))
    return data

def building_returns(data):
    returns = []
    for instance in data:
        percentage = round(((instance[1]-instance[0])/instance[0])*100,3)
        returns.append(percentage)
    return returns
