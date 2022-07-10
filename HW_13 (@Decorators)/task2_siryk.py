import functools

def stop_words(words: list):
    '''
    :param words: list of stop words
    :return: list with replaced stop words with * inside the decorated function
    '''
    def me(func):
        @functools.wraps(func)
        def wrapper(*args):
            d = func(*args)
            for bad in words:
                d = d.replace(bad, '*')
            return d
        return wrapper
    return me


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print(create_slogan.__name__)