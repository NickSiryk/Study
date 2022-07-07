'''work with simple functions'''

import math

def square(a):
    '''function square that takes 1 argument — the side of the square, and returns 3 values (using a tuple):
    the perimeter of the square,
    the area of the square,
    and the diagonal of the square.'''

    if a.isdigit():
        a = float(a)
        p = a * 2
        s = a ** 2
        d = round((math.sqrt(2) * a), 2)
        return (p, s, d)
    else:
        return 'Should be a digit!'

print(square(input('Size of square, please: ')))

def season(n):
    '''
    function that convert number of month to rime o  the time of the year to which this month belongs
    :param n: the number of the month (from 1 to 12)
    :return: winter, spring, summer or autumn
    '''

    seas_dict = {'12': 'Winter', '1': 'Winter', '2': 'Winter', '3': 'Spring', '4': 'Spring',\
                 '5': 'Spring', '6': 'Summer', '7': 'Summer', '8': 'Summer', '9': 'Autumn', \
                 '10': 'Autumn', '11': 'Autumn'}
    if n.isdigit and 0 < int(n) <= 12:
        return seas_dict[n]
    else:
        return 'Should be a digit from 1 to 12!'


print(season(input('Mounth, please: ')))
