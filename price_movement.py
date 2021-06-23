def building_percentages(number_of_decimals, lower_percentage, upper_percentage):
    number_of_decimals = 10**number_of_decimals
    low = lower_percentage*number_of_decimals
    up  = (upper_percentage)*number_of_decimals
    percentages = [x/number_of_decimals for x in range(low, up)]
    return percentages

def displaying_prices(price, percentages):
    for percentage in percentages:
        potential_price = round(price*(1+percentage/100),2)
        print(f'If {price} changes {percentage}%, the new price is {potential_price}.')
        print('-----------------------------------------------------------------------')

def displaying_percentages(price):
    change = [x*0.5 for x in range(-40,41)]   
    for unit in change:
        potential_price = price + unit 
        percentage = round(((unit)/(price))*100,3)
        print(f'If {price} changes to {potential_price} this represents a change of {percentage}%.')
        print('-----------------------------------------------------------------------')
        
def displaying_prices_returns(buy_in_price, percentages, number_shares):
    for percentage in percentages:
        potential_price = round(buy_in_price*(1+percentage/100),2)
        potential_return = round((potential_price - buy_in_price)*number_shares,2)
        print(f'If {buy_in_price} changes {percentage}%, the new price is {potential_price} with a return of {potential_return}.')
        print('-----------------------------------------------------------------------')
