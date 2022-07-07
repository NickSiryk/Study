'''program that emulate different type of game dice'''

import random


def dice():
   '''Standart dice emulator. No values needed!'''
   return random.randint(1, 6)


def graph_dice():
    '''Graph dice emulator. No values needed!'''
    graph = ('⚀', '⚁', '⚂', '⚃', '⚄', '⚅')
    return random.choice(graph)


def universal_dice(n=6):
   '''Universal-sized dice emulator'''
   return random.randint(1, n)


def vedro_kubov(n=6, k=1):
    '''Universal-sized dice emulator with multiple attempts'''
    dice_list = []
    for i in range(0, k):
        dice_list.append(random.randint(1, n))
    return dice_list


if __name__ == '__main__':
    #3
    print(dice())

    #4
    print(graph_dice())

    #5
    size = input('Print the number of sizes, or press enter: ').strip()
    if size.isdigit():
        print(universal_dice(int(size)))
    else:
        print(universal_dice())

    #6
    size_vedro = input('Print the number of sizes, or press enter: ').strip()
    att_vedro = input('Print the number of attempts, or press enter: ').strip()
    if size_vedro.isdigit():
        if not att_vedro.isdigit():
            print(vedro_kubov(int(size_vedro)))
        else:
            print(vedro_kubov(int(size_vedro), int(att_vedro)))
    else:
        if att_vedro.isdigit():
            print(vedro_kubov(k=int(att_vedro)))
        else:
            print(vedro_kubov())
