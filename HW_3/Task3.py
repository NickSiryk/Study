name = 'nick'
count = 0
print('This is a guess game. You need to guess my name.\nLet\'s start.')
while True:
    count += 1
    check = input('Print your variant here (If You wanna stop, just write some digit): ').strip().lower()
    if check.isdigit():
        print(f'You made {count} attempts.')
        print('Bye')
        break
    elif check == name:
        print('NOSTRADAMUS!')
        print(f'You made {count} attempts.')
        break
    else:
        print('Wrong( Try one more time.')
