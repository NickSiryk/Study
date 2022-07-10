class Mathematician:
    '''
    A class Mathematician which is a helper class for doing math operations on lists
    The class doesn't take any attributes and only has methods
    '''
    def square_nums(self, math_list):
        '''
        :param math_list: list of integers
        :return: the list of squares
        '''
        math_list_new = [i * i for i in math_list]
        return math_list_new

    def remove_positives(self, math_list):
        '''
        :param math_list: list of integers
        :return: the list without positive numbers
        '''
        math_list_new = [i for i in math_list if i < 0]
        return math_list_new

    def filter_leaps(self, math_list):
        '''
        :param math_list: list of dates (integers) and
        :return: the list without those that are not 'leap years'
        '''
        math_list_new = [i for i in math_list if i % 4 == 0 or i % 100 == 0 or i % 400 == 0]
        return math_list_new


m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
