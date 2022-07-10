import functools

def logger(func):
    '''
    A decorator that prints a function with arguments passed to it.
    '''
    @functools.wraps(func)
    def wrapper(*args):
        args = str(args)
        f = f'{func.__name__} called with {args[1:-1]}'
        return f
    return wrapper
    pass


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(4,5))
print(square_all(4,5))