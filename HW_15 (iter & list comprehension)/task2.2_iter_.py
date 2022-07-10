class Phonefil:
    '''
    Number filter and iterator class
    '''
    def __init__(self, ls, task):
        '''
        :param ls: The list of text variables with phones is set
        :param task: number of task
            - 7:int Return only phones that are numbers beginning with "097"
            - 8:int Return only phones that are numbers beginning with "097" or "050"
            - 9:int Return only phones that are numbers beginning with "097" or "050"
                    and adding the international code ("+380") to them and getting rid of spaces.
        '''
        self.ls = ls
        self.task = task

    def __iter__(self):
        return Phonefil_iter(self.ls, self.task)


class Phonefil_iter:
    def __init__(self, ls_g, case):
        self.ls_g = ls_g
        self.case = case
        self.counter = -1

    def __next__(self):
        if self.counter < len(self.ls_g) - 1:
            self.counter += 1
            if self.case == 7:
                bool = self.ls_g[self.counter][:3] == '097'
                if bool:
                    return self.ls_g[self.counter]
                else:
                    return self.__next__()
            elif self.case == 8:
                bool = self.ls_g[self.counter][:3] == '097' or self.ls_g[self.counter][:3] == '050'
                if bool:
                    return self.ls_g[self.counter]
                else:
                    return self.__next__()
            elif self.case == 9:
                bool = self.ls_g[self.counter][:3] == '097' or self.ls_g[self.counter][:3] == '050'
                if bool:
                    return f'+38{self.ls_g[self.counter].replace(" ", "")}'
                else:
                    return self.__next__()
            else:
                raise ValueError('No such iterator!')
        else:
            raise StopIteration


phones = ['044 225 73 39', '099 116 30 87', '094 129 81 69', '094 127 04 85', '044 222 74 33', '044 353 55 31',
          '097 921 27 09', '094 550 50 02', '044 362 96 00', '097 853 55 81', '097 120 95 90', '099 752 22 97',
          '050 761 49 45', '094 497 75 09', '094 498 89 53', '094 496 13 91', '094 497 35 13', '094 497 75 69',
          '050 063 52 97', '050 530 97 71', '044 227 16 63', '056 785 55 19', '068 450 69 13', '097 001 42 67',
          '096 097 58 16', '094 497 34 37', '094 097 12 17', '094 497 75 69', '097 497 75 97', '094 497 34 85',
          '094 496 52 54']

print('2.7:')
t = Phonefil(phones, 7)
for i in t:
    print(i)

print('2.8:')
t = Phonefil(phones, 8)
for i in t:
    print(i)

print('2.9:')
t = Phonefil(phones, 9)
for i in t:
    print(i)


