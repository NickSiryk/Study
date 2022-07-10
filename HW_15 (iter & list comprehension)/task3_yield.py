def GreatNumerator(ls: list):
    '''
    A GreatNumerator class that receive a list of strings,
    and then output each of the strings with an added number.
    '''

    for count, i in enumerate(ls):
        yield f'{count} {i}'


def Phonefil(ls: list, task: int):
    '''
    :param ls: The list of text variables with phones is set
    :param task: number of task
        - 7:int Return only phones that are numbers beginning with "097"
        - 8:int Return only phones that are numbers beginning with "097" or "050"
        - 9:int Return only phones that are numbers beginning with "097" or "050"
                and adding the international code ("+380") to them and getting rid of spaces.
    :return: filtered iterator
    '''
    if task == 7:
        for i in ls:
            if i[:3] == '097':
                yield i
    elif task == 8:
        for i in ls:
            if i[:3] == '097' or i[:3] == '050':
                yield i
    elif task == 9:
        for i in ls:
            if i[:3] == '097' or i[:3] == '050':
                yield f'+38{i.replace(" ", "")}'

#Task 3.1
task_ex = ['111', 'cat', 'got', 'ddd', '222']
for i in GreatNumerator(task_ex):
    print(i)

#Task 3.7 - 3.9
phones = ['044 225 73 39', '099 116 30 87', '094 129 81 69', '094 127 04 85', '044 222 74 33', '044 353 55 31', '097 921 27 09', '094 550 50 02', '044 362 96 00', '097 853 55 81', '097 120 95 90', '099 752 22 97', '050 761 49 45', '094 497 75 09', '094 498 89 53', '094 496 13 91', '094 497 35 13', '094 497 75 69', '050 063 52 97', '050 530 97 71', '044 227 16 63', '056 785 55 19', '068 450 69 13', '097 001 42 67', '096 097 58 16', '094 497 34 37', '094 097 12 17', '094 497 75 69', '097 497 75 97', '094 497 34 85', '094 496 52 54']
print('3.7:')
for i in Phonefil(phones, 7):
    print(i)

print('3.8:')
for i in Phonefil(phones, 8):
    print(i)

print('3.9:')
for i in Phonefil(phones, 9):
    print(i)