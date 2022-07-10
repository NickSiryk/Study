'''
Practice with recursion
'''

def rev1(st):
    '''
    A function that rotates letters in a word (rewrites it backwards)
    '''
    if len(st) < 2:
        return st
    else:
        return st[-1] + rev1(st[1:-1]) + st[0]

def rev2(st):
    '''
    A function that rotates words in a sentence separated by spaces. (rewrites it backwards)
    '''
    st = st.split(maxsplit=1)
    if len(st) < 2:
        return st[0]
    else:
        st[0], st[1] = rev2(st[1]), st[0]
        return ' '.join(st)

def str_sum(chislo):
    '''
    A function that receives a string with a number and displays the sum of its digits
    '''
    if chislo.isdigit():
        if len(chislo) == 1:
            return int(chislo)
        else:
            return int(chislo[0])+str_sum(chislo[1:])
    else:
        raise ValueError('SHOULD BE A DIGIT!')

def int_sum(chislo):
    '''
    A function that takes a pure number (int) and outputs the sum of its digits. (no conversion to str)
    '''
    if chislo < 10:
        return chislo
    else:
        return chislo % 10 + int_sum(chislo // 10)

assert rev1('Бла-бла-бла') == 'алб-алб-алБ'
assert rev2('магистр Йода так говорит поскольку джедай') == 'джедай поскольку говорит так Йода магистр'
a = '12345'
assert str_sum(a) == 15
a = 5001001001
assert int_sum(a) == 8