import functools


def arg_rules(type_: type, max_length: int, contains: list):
    '''
    A decorator that validates arguments passed to the function.
    :param type_: type of args
    :param max_length: len of args
    :param contains: list of symbols that an argument should contain
    :return:
        If some of the rules' checks returns False and print the reason it failed;
        Otherwise, return the result
    '''
    def me(func):
        @functools.wraps(func)
        def wrapper(*args):
            if type(*args) != type_:
                print('Name should be a "str" type!')
                return False
            elif len(*args) > max_length:
                print('Name is too long!')
                return False
            elif len([i for i in contains for j in args if i not in j]) != 0:
                print(f'Should contain {contains}')
                return False
            else:
                return func(*args)
        return wrapper
    return me
    pass


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
print(create_slogan.__name__)
