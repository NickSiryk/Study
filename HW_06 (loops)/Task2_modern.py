'''function which takes as input two dicts (stock and prices), then computes and returns the total price of stock

(with randomly generated task and simple interface)
'''


import random


def t_prices(stock_in: dict, prices_in: dict):     # func for calculation of total price of stock
    tot_price = 0
    for st in stock_in.keys():
        for pr in prices_in.keys():
            if st == pr:
                tot_price += stock_in[st] * prices_in[pr]
    return tot_price


def string_randomizer(number1: int, length: int):  # func for making a random string (func from task1)
    alph1 = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N'
        , 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    alph2 = ['A', 'E', 'I', 'O', 'U', 'Y']

    string_all1 = []
    for j in range(number1):  # number of words
        string_word = ''
        for g in range(random.randint(1, length)):  # length of words
            rnd = [random.choice(alph1), random.choice(alph2)]  # choosing a type of letter
            string_word += random.choice(rnd)
        string_all1.append(string_word)
    return string_all1


def number_input(input_str: str, error_str: str):   # func, which take the input and error messages and return float number
    while True:
        try:
            num_input = float(input(input_str))
        except ValueError:
            print(error_str)
        else:
            break
    return num_input


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


while True:
    dialogue = input('Welcome in stock counter program! Here is Your choose option:\n'
                     '1 - take the task dictionaries\n'
                     '2 - choose random dictionaries\n'
                     '3 - print your own dictionaries\n'
                     '4 - exit\n>> ')
    dialogue = dialogue.strip()
    if dialogue == '1':  # work with task dicts
        print(f'Our dicts is:\nStock: {stock_task}\nPrices: {prices_task}')
        sum_print = t_prices(stock_task, prices_task)   # Using func for calculation
        print(f'Total stock price is {sum_print}')
        break
    elif dialogue == '2':  # working with random dicts
        num_of_words = int(number_input('Choose number of elements: ', 'Should be a number'))   # using the input digit func
        len_of_words = int(number_input('Choose max length of elements: ', 'Should be a number'))    # using the input digit func
        keys = string_randomizer(num_of_words, len_of_words)  # using randomizer for make list of keys
        stock_rand = {key: (random.randint(0, 50)) for key in keys}  # dict of stock by comprehension
        prices_rand = {key: round((random.random()+random.randint(0, 15)), 1) for key in keys}  # dict of prices by comprehension
        print(f'Our dicts is:\nStock: {stock_rand}\nPrices: {prices_rand}')
        sum_print = t_prices(stock_rand, prices_rand)  # Using func for calculation
        print(f'Total stock price is {sum_print}')
        break
    elif dialogue == '3':   # Working with user dicts
        stock_inp = {}      # Empty dict for stock
        prices_inp = {}     # Empty dict for price
        num_of_words = int(number_input('Choose number of elements: ', 'Should be a number'))    # Size of our dicts by input func
        for i in range(num_of_words):    # input data loop
            key = input(f'Print the name of element number {i+1}: ')
            number = int(number_input(f'Print the number of {key}: ',  'Should be a number'))
            stock_inp[key] = number     # Add a number of stock in dict
            price = float(number_input(f'Print the price of {key}: ', 'Should be a digit!'))
            prices_inp[key] = price     # Add a price of stock in dict
        print(f'Our dicts is:\nStock: {stock_inp}\nPrices: {prices_inp}')
        sum_print = t_prices(stock_inp, prices_inp)  # Using func for calculation
        print(f'Total stock price is {sum_print}')
        break
    elif dialogue == '4':   # exit from program
        break
    else:
        print('Sorry, I don\'t know this option')   # exception