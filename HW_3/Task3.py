name = 'nick'
count = 0
print('This is a guess game. You need to guess my name.\nLet\'s start.')
while True:
    check = input('Print your variant here (If You wanna stop, just write some digit): ').strip().lower()
    if check.isdigit():
        print('Bye')
        break
    elif check == name:
        print('NOSTRADAMUS!')
        break
    else:
        print('Wrong( Try one more time.')
