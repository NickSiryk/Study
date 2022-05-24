import random


def number_input(input_str: str, error_str: str):   # func, which take the input and error messages and return float number
    while True:
        try:
            num_input = float(input(input_str))
        except ValueError:
            print(error_str)
        else:
            break
    return num_input


def task1(args: list):
    max_len = 1
    max_run = args[0]
    m_len = 1
    for i in range(0, len(args)-1):
        run = args[i]
        if run == args[i + 1]:  # 1,2,3,4,4,4,4,4,4,5,6,7,4,2,2,5
            m_len += 1
        else:
            m_len = 1
        if max_len < m_len:
            max_len = m_len
            max_run = run
    return [max_len, max_run]


def randomizer_1():
    num_input = int(number_input('Choose a number of elements: ', 'Should be a number'))
    random_data = [str(random.randint(1, 10)) for i in range(num_input)]
    return random_data

stock_task = [1,2,3,4,4,4,4,4,4,5,6,7,4,2,2,5]

dialogue = input('Welcome in longest consecutive run counter program! Here is Your choose option:\n'
                     '1 - Take the task list\n'
                     '2 - Choose random list\n'
                     '3 - Print your own list\n'
                     '4 - Exit\n>> ')

while True:
    if dialogue == '1':  # work with task dicts
        print(f'Our list is: {stock_task}')
        print(task1(stock_task))
        break
    elif dialogue == '2':  # working with random dicts
        stock_task = randomizer_1()
        print(f'Our list is: {stock_task}')
        print(task1(stock_task))
        break
    elif dialogue == '3':  # Working with user dicts
        stock_task = []
        num_input = int(number_input('Choose a number of elements: ', 'Should be a number'))
        for i in range(num_input):
            stock_task.append(input('Print next element:'))
        print(f'Our list is: {stock_task}')
        print(task1(stock_task))
        break
    elif dialogue == '4':  # exit from program
        break
    else:
        print('Sorry, I don\'t know this option')  # exception


