'''a simple calculator using func'''

import math


def make_operation(sign, *task):
    if sign == '-':
        deduct = (task[i] for i in range(1, len(task)))
        answer = task[0] - math.fsum(deduct)
    elif sign == '+':
        answer = math.fsum(task)
    elif sign == '*':
        answer = math.prod(task)
    else:
        answer = 'We have not this option('
    return answer


print('Welcome in a simple calc program!\nwe can operate the following functions: "+", "-", "*"')
sel = input('Choose the function by sign, and print the arguments\
in follow format (+, 2, 3, 4): ').strip()
user_task = sel.split(', ')
user_sign = user_task[0]
ins_task = (int(user_task[i]) for i in range(1, len(user_task)))
print(f'Answer is: {make_operation(user_sign, *ins_task)}')

