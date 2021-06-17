from sequences import building_set_cumulative_sequences, builiding_sequences
from sequences import display_cumulative_sequences, display_sequences
from matplotlib import pyplot as plt
from numpy import mean, std, amax, amin
from returns import read_data, building_returns

def key_values(distribution):
    """
    returns: mean, standard deviation, max_value and min_value 
    """ 
    u = mean(distribution)
    s = std(distribution)
    maximum = amax(distribution)
    minimum = amin(distribution)
    return (u, s, maximum, minimum)

def building_target_range(returns, lower_bound, upper_bound):
    target_sequences = []
    for percentage in returns:
        if percentage >= lower_bound and percentage <= upper_bound:
            target_sequences.append(percentage)
    target_sequences.sort()
    return target_sequences

def printing_probabilities(returns, target_returns):
    ratio = len(target_returns)/len(returns)
    ratio = round(ratio*100 ,2)
    if ratio != 0:
        lower_bound = target_returns[0]
        upper_bound = target_returns[-1]
        print(f'The probability of having values between {lower_bound}% and {upper_bound}% is: {ratio}%')
    else:
        print('The probability is this range is 0%.')

def positive_end_probabilistic_distribution(distribution, intervals):
    positive_returns = building_target_range(distribution, 0, amax(distribution))
    average, std, _ , _ = key_values(positive_returns)
    values = range(1,intervals)
    print(f'Mean: {average}, Standard Deviation: {std}')
    print('--------------------------------------------------------------------------------------')
    for value in values:
        lower_bound = (value/10)*std
        upper_bound = ((value+1)/10)*std
        target = building_target_range(positive_returns, lower_bound, upper_bound)
        print(f'Number of standard deviations away: ' + str(value/10))
        printing_probabilities(positive_returns, target)
        print('--------------------------------------------------------------------------------------')

def cumulative_positive_end_probabilistic_distribution(distribution, intervals):
    positive_returns = building_target_range(distribution, 0, amax(distribution))
    average, std, _ , _ = key_values(positive_returns)
    values = range(1,intervals)
    print(f'Mean: {average}, Standard Deviation: {std}')
    print('--------------------------------------------------------------------------------------')
    for value in values:
        upper_bound = ((value)/10)*std
        target = building_target_range(positive_returns, 0, upper_bound)
        print(f'Number of standard deviations away: ' + str(value/10))
        printing_probabilities(positive_returns, target)
        print('--------------------------------------------------------------------------------------')

def negative_end_probabilistic_distribution(distribution, intervals):
    negative_returns = building_target_range(distribution, amin(distribution), 0)
    average, std, _ , _ = key_values(negative_returns)
    values = range(1,intervals)
    print(f'Mean: {average}, Standard Deviation: {std}')
    print('--------------------------------------------------------------------------------------')
    for value in values:
        lower_bound = -((value+1)/10)*std
        upper_bound = -(value/10)*std
        target = building_target_range(negative_returns, lower_bound, upper_bound)
        print(f'Number of standard deviations away: ' + str(value/10))
        printing_probabilities(negative_returns, target)
        print('--------------------------------------------------------------------------------------')

def cumulative_negative_end_probabilistic_distribution(distribution, intervals):
    negative_returns = building_target_range(distribution, amin(distribution), 0)
    average, std, _ , _ = key_values(negative_returns)
    values = range(1,intervals)
    print(f'Mean: {average}, Standard Deviation: {std}')
    print('--------------------------------------------------------------------------------------')
    for value in values:
        lower_bound = -(value/10)*std
        target = building_target_range(negative_returns, lower_bound, 0 )
        print(f'Number of standard deviations away: ' + str(value/10))
        printing_probabilities(negative_returns, target)
        print('--------------------------------------------------------------------------------------')

def options_chain_probabilities(percentages, central_price, number_strikes):
    strikes = [(central_price + x) for x in range(-number_strikes, number_strikes + 1)]
    for strike in strikes:
        bound = round(100*(strike-central_price)/(central_price),2)
        if bound > 0:
            positive_returns = building_target_range(percentages, 0, amax(percentages))
            target = building_target_range(positive_returns, 0, bound)
            print(f'At the current price of {central_price}, values ranging below {strike}:')
            printing_probabilities(percentages, target)
            print('--------------------------------------------------------------------------------------')
        else:
            negative_returns = building_target_range(percentages, amin(percentages), 0)
            target = building_target_range(negative_returns, bound, 0)
            print(f'At the current price of {central_price}, values ranging above {strike}:')
            printing_probabilities(percentages, target)
            print('--------------------------------------------------------------------------------------')

def plotting_histogram_distribution(x_axis):
    bins = range(-15,15)
    plt.hist(x_axis, bins, color = 'r')
    plt.show()

def plotting_scatter(x_axis):
    plt.plot(x_axis, marker = 'o', color = 'g')
    plt.show()

def plotting_cartesian(trends):
    for trend in trends:
            plt.plot(trend, color = 'b', linestyle = '-', marker = '.') 
    plt.show()

csv_file = 'TQQQ_Week_Max.csv'
data = read_data(csv_file)
percentages = building_returns(data)
runs = builiding_sequences(percentages, 0, amax(percentages))
cum_runs = building_set_cumulative_sequences(runs)
display_cumulative_sequences(cum_runs)
options_chain_probabilities(percentages, 109, 16) 