'''
Program to compare work time of different sorting methods
'''

import time
import sort1    # First sort
import sort2    # Second sort
import random
import csv

# start a global counter
t1 = time.perf_counter()

def stend(f, n, *args, **kwargs):
    '''
    :param f: sort function
    :param n: number of sorting times
    :return: average sorting time
    '''

    t = []  # list of results

    for i in range(n):
        t1 = time.perf_counter()
        f(*args, **kwargs)
        t2 = time.perf_counter()
        t.append(t2-t1)

    a = sum(t)/len(t)
    return f'time of {n} iterations of "{f.__module__}.{f.__name__}" function is: {a:.7f} secs'

# Creates a test list
k = 10  # number of sorting times
N = 10000   # len of list
r = list(range(N))
random.shuffle(r)

# Sorting
print(stend(sort1.selection_sort, k, r))
print(stend(sort2.selection_sort, k, r))
print(stend(sorted, k, r))
print(stend(r.sort, k))

# end a global counter
t2 = time.perf_counter()
print(f'All time of work: {t2-t1}')