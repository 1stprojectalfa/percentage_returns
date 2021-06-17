from itertools import groupby

def builiding_sequences(returns, lower_bound, upper_bound):
    filter_function = lambda x: x >= lower_bound and x <= upper_bound 
    sequences = [list(k) for i, k  in groupby(returns, filter_function)]
    return sequences

def _building_cumulative_sequence(percentages):
    values = []
    values.append(100)

    for value in percentages:
        q_i = values[-1]
        q = round(q_i*(1 + value/100),3)
        values.append(q)
    values.remove(100)

    for i in range(len(values)):
        values[i] = round(values[i] - 100,3)
    return values

def building_set_cumulative_sequences(sequences):
    cumulative_sequences = []
    for sequence in sequences:
        cumulative_sequence = _building_cumulative_sequence(sequence)
        cumulative_sequences.append(cumulative_sequence)
    return cumulative_sequences

def filtering_sequences(sequences, length):
    target_sequences = []
    for sequence in sequences:
        if len(sequence) == length:
            target_sequences.append(sequence)
    return target_sequences

def building_cumulative_distribution(sequences):
    sequence_distribution = []
    for sequence in sequences:
        sequence_distribution.append(sequence[-1])
    return sequence_distribution

def building_lengths_distribution(sequences):
    lengths_distribution = []
    for sequence in sequences:
        lengths_distribution.append(len(sequence))
    return lengths_distribution

def display_sequences(runs):
    for run in runs:
        print(f'Periods {len(run)}, run: {run} and sum: {round(sum(run),3)}%')

def display_cumulative_sequences(cumulative_runs):
    for run in cumulative_runs :
        print(f'Periods {len(run)}, cumulative run: {run}, with a total change of: {run[-1]}%.')