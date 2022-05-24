import math
while True:
    n = input('write a number, please: ').strip()
    if n.isdigit():
        n = int(n)
        break
    else:
        print('Something went wrong. Try one more time.')

for i in range(0, n+1):
    for j in range(0, n+1):
        if i == 0:
            print('', j, end='')
            continue
        if j == 0:
            if i < 10:
                print('', i, end=' ')
            else:
                print(i, end=' ')
            continue
        if math.gcd(i, j) == 1:
            if j < 10:
                print('*', end=' ')
            else:
                print(' *', end=' ')
        else:
            if j < 10:
                print(' ', end=' ')
            else:
                print('  ', end=' ')
    print()

