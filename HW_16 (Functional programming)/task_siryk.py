'''
Analyze the attached log
with counting the work time of functions by decorator
'''

import functools
import time
import datetime as dt

big_file = 'red_apple.log'

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def all_tr():
    '''
    :return: how many bytes were spent on traffic in general
    '''
    with open(big_file) as f:
        lines = (line.rsplit(maxsplit=2)[2] for line in f)
        bytes = (int(byte) for byte in lines if byte.isdigit())
        return sum(bytes)


@timer
def task_1():
    '''
    :return: how many bytes were spent on traffic for all responses with the code "200"
    '''
    with open(big_file) as f:
        lines = (line.rsplit(maxsplit=2) for line in f)
        inds = (int(ind[2]) for ind in lines if ind[1] == '200' and ind[2].isdigit())
        return sum(inds)


@timer
def task_2():
    '''
    :return: how many bytes were spent on traffic for all responses with the code "404"
    '''
    with open(big_file) as f:
        lines = (line.rsplit(maxsplit=2) for line in f)
        inds = (int(ind[2]) for ind in lines if ind[1] == '404' and ind[2].isdigit())
        return sum(inds)


@timer
def task_3():
    '''
    :return: The total number of all requests without exception.
    '''
    with open(big_file) as f:
        asks = (1 for ask in f)
        return sum(asks)

@timer
def task_4():
    '''
    :return: the number of all responses with the code "200"
    '''
    with open(big_file) as f:
        asks = (1 for line in f if line.rsplit(maxsplit=2)[1] == '200')
        return sum(asks)

@timer
def task_5():
    '''
    :return: the number of all responses with the code "404"
    '''
    with open(big_file) as f:
        asks = (1 for line in f if line.rsplit(maxsplit=2)[1] == '404')
        return sum(asks)

@timer
def task_6_1():
    '''
    :return: the average bytes spent on a 200 reques
    '''
    return task_1()/task_4()

@timer
def task_6_2():
    '''
    :return: the average bytes spent on a 404 reques
    '''
    return task_2()/task_5()

@timer
def task_7():
    '''
    :return: sorted list of all unique ip-addresses from which requests came
    '''
    with open(big_file) as f:
        import socket
        lines = set(line.split(maxsplit=1)[0] for line in f)
        return tuple(sorted(lines, key=lambda i: socket.inet_aton(i)))

@timer
def task_8():
    '''
    :return: number unique ip-addresses from which requests came
    '''
    with open(big_file) as f:
        lines = set(line.split(maxsplit=1)[0] for line in f)
        return len(lines)

@timer
def task_9(start, stop):
    '''
    :param start: beginning of period
    :param stop: end of period
    :return: set of those ips, requests from which came in a certain period of time
    '''

    before = dt.datetime.strptime(start, '%H:%M:%S').time()
    after = dt.datetime.strptime(stop, '%H:%M:%S').time()

    with open(big_file) as f:
        lines = (line.split(maxsplit=4) for line in f)
        times = ((tim[0], dt.datetime.strptime(tim[3].split(':', maxsplit=1)[1], '%H:%M:%S').time()) for tim in lines)
        ips = (ip[0] for ip in times if before < ip[1] <= after)
        ans = set(ips)
        return ans


def task_10():
    '''
    :return: When do more people visit the site - before noon or after noon?
    '''
    before = len(task_9('00:00:00', '12:00:00'))
    after = len(task_9('12:00:00', '23:59:59'))
    print(f'Before: {before}')
    print(f'After: {after}')
    if before > after:
        return 'Before noon more'
    elif before < after:
        return 'After noon more'
    else:
        return 'Equal'

# all = all_tr()
# one = task_1()
# two = task_2()
# three = task_3()
# four = task_4()
# five = task_5()
# six_1 = task_6_1()
# six_2 = task_6_2()

# print(f'Total all: {all}')
# print(f'Total 200: {one}')
# print(f'Total 404: {two}')
# print(f'Total all att: {three}')
# print(f'Total 200 att: {four}')
# print(f'Total 404 att: {five}')
# print(f'Total 200 b/a: {six_1:.0f}')
# print(f'Total 404 b/a: {six_2:.0f}')

# print(task_7())

# print(task_8())

# print(task_9('00:00:00', '12:00:00'))

# print(task_10())
