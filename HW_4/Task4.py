import random
import math
print('Let\'s play a MATH QUIZ!\nRules: I\'ll give You math expression.\
\nYou need to answer!\nYou play up to 3 right answers!')
count = 0
while count < 3:
    switch = random.randint(1, 4)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if switch == 1: # "+"
        ans = math.fsum([num1, num2])
        guess = input(f'{num1} + {num2} = ')
    elif switch == 2:  # "-"
        ans = num1 - num2
        guess = input(f'{num1} - {num2} = ')
    elif switch == 3:  # "*"
        ans = math.prod([num1, num2])
        guess = input(f'{num1} * {num2} = ')
    elif switch == 4:  # "pow"
        ans = math.pow(num1, num2)
        guess = input(f'{num1}^{num2} = ')
    try:
        guess = float(guess)
    except ValueError:
        print('I need numbers!')
    else:
        if ans == guess:
            count += 1
            print('correct!')
        else:
            print(f'Nope! Correct answer is {ans}')
