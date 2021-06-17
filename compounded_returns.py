from math import log

percentages = [-1]
c = 10_000

def compounded_fixed_returns(percentage, initial_c, periods):
    q = round(initial_c*(1 + percentage/100)**periods, 2)
    return q

def compounded_variable_returns(percentages, initial_c):
    values = []
    values.append(initial_c)
    for percentage in percentages:
        q_i = values[-1]
        q = round(q_i*(1 + percentage/100),2)
        values.append(q)
    return values

def printing_potential_periods(percentages, initial_c, final_c):
    ratio = final_c/initial_c
    for percentage in percentages:
        t = round(log(ratio)/log(1 + (percentage/100)),0)
        print(f'{initial_c:_} turns into {final_c:_} in {t} periods with an compound interest of {percentage}%.')
