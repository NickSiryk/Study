'''function which takes as input two dicts (stock and prices), then computes and returns the total price of stock'''

def t_prices(stock_in: dict, prices_in: dict):     # func for calculation of total price of stock
    tot_price = 0
    for st in stock_in.keys():
        for pr in prices_in.keys():
            if st == pr:
                tot_price += stock_in[st] * prices_in[pr]
    return tot_price


stock_task = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices_task = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print(f'Our dicts is:\nStock: {stock_task}\nPrices: {prices_task}')
sum_print = t_prices(stock_task, prices_task)   # Using func for calculation
print(f'Total stock price is {sum_print}')