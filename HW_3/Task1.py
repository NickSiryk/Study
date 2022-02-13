a = 0
while a < 6:
    print('If You want to stop all of this, just print "Q"')
    long_string = input('Write Your string, please: ')
    if long_string == 'Q':
        print('See You!')
        break
    elif len(long_string) < 2:
        print('Empty String')
    else:
        print(long_string[0:2]+long_string[-2:len(long_string)])
    a += 1
else:
    print('More than 5 prints. I need a vacation. Bye!')