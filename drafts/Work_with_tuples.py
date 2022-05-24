#  Average

import random
list1 = [random.randint(1, 100) for i in range(50)]
print(list1)

counter = 0
suma = 0
while counter < len(list1):
    suma += list1[counter]
    counter += 1
print(suma / counter)
print(sum(list1) / len(list1))

# reverse
counter = 0
r_counter = len(list1) - 1
while counter < len(list1) / 2:
    list1[counter], list1[r_counter] = list1[r_counter], list1[counter]
    counter += 1
    r_counter -= 1
print(list1)

#  copy of lists
import copy
counter = 0
list3 = []
while counter < len(list1):
    list3.append(copy.copy(list1[counter]))
    counter += 1
print(list3)

# clear empty tuple in list

up = [() if i % 3 == 0 else (random.randint(1, 10),) for i in range(10)]
print(up)
for i in up:
    if len(i) == 0:
        del up[up.index(i)]
print(up)


# Comprehantion
num_3 = [x for x in range(700, 4000, 130)]
print(num_3)

#  find doubles in list
import random
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'\
    , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
adress = ()
list = {}
for j in range(200):
    name = ''
    for i in range(2):
        name += random.choice(alph)
    adress = adress + (name,)
print(adress)

counter = 1
for first in adress:
    for second in range(counter, len(adress)):
        if first == adress[second]:
            if list.get(first):
                for k in list[first]:
                    if k == second:
                        break
                else:
                    list[first].append(second)
            else:
                list[first] = [counter - 1, second]
    counter += 1
print(list)
