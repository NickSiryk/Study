import random
str = list(input('Print something: '))  #now it's a list
for i in range(1, 6):
    random.shuffle(str)  # shuffle list
    print(''.join(str))  # back to string