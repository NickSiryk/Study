'''program that generates a random number between 1 and 10 and lets the user guess'''

import random
print('Let\'s play a GUESS GAME!')
num = random.randint(1, 10)
count = 0
while True:
    while True:
        guess = input('Guess, what number from 1 to 10 was generated? ').strip()
        if guess.isdigit():
            guess = int(guess)
            count += 1
            break
        else:
            print('It should be a number!)')
    if num == guess:
        if count == 1:
            print('NOSTRADAMUS!')
        else:
            print(f'Correct! The number was {num}! You made {count} guesses!')
        break
    elif guess < num:
        print('Bigger!')
    elif guess > num:
        print('Smaller!')
