'''
A GreatNumerator class that receive a list of strings,
and then output each of the strings with an added number.
'''


class GreatNumerator:
    def __init__(self, ls):
        self.ls = ls

    def __iter__(self):
        return GreatIterator(self.ls)


class GreatIterator:
    def __init__(self, ls_g):
        self.ls_g = ls_g
        self.counter = 0

    def __next__(self):
        if self.counter < len(self.ls_g):
            f = f'{self.counter} {self.ls_g[self.counter]}'
            self.counter += 1
            return f
        else:
            raise StopIteration


lists = ['111', 'cat', 'got', 'ddd', '222']
t = GreatNumerator(lists)
for i in t:
    print(i)
