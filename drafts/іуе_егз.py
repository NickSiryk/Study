import random

def func_1 (*list_1):
    list_1 = list(list_1)
    list_2 = list(set(list_1))
    for i in list_2:
        list_1.remove(i)
    list_1 = list(set(list_1))
    return list_1

list_1 = [random.randint(1, 4) for i in range(random.randint(30, 35))]
print(list_1)
print(func_1(*list_1))