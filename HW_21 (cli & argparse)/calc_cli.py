'''
A calculator with a command line interface
'''

import sys
version = '0.0.1'
args = sys.argv

def calculator(args, more = False):
    '''
    :param args: the first term, the second term and the action between them
    :param more: if TRUE print not just the answer, but the entire expression, like this:
    :returns:
        standard: calc.py 1 2 -
                 -1
        more: calc.py 1 2 - -v
                 1 - 2 = -1
    '''

    try:
        # parse elements
        first = float(args[1])
        second = float(args[2])
        proc = args[3]

        if proc == '-':
            ans = first - second
        elif proc == '+':
            ans = first + second
        elif proc == '*':
            ans = first * second
        elif proc == '/':
            ans = round(first / second, 2)

        if more:
             return (f'{first} {proc} {second} = {ans}')
        else:
            return ans

    except ValueError:
        pass

# switch checking
if '-v' in args:
    # asks long form
    answ = calculator(args, True)
else:
    # asks short form
    answ = calculator(args)

if '-h' in args or '--help' in args:
    # Help information
    answ = ('syntax: _first_ _second_ _proc_ -v\n'
          '_first_    - first argument\n'
          '_second_   - second argument\n'
          '_proc_     - symbol of procedure. "-", "+", "*", "/"\n'
          '-v       - optional long version\n')

if '-f' in args:
    # Writes result to the file

    f = open('result.txt', 'w')
    f.write(answ)
    f.close()

print(answ)