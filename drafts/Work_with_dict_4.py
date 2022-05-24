#  Write an address book, using dictionaries, where I can query contact info,
#  insert new contact, delete contact information, exit address book program.
#  Also add key-value for number of friend of each contact and calculate and average
import random
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'\
    , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
adress = {}
for j in range(10):
    name = ''
    for i in range(4):
        name += random.choice(alph)
        num_tel = [random.randint(1000000000, 9999999999), random.randint(1,10)]
    adress[name] = num_tel

while True:
    try:
        text = input(f'Список друзей: {[i for i in adress.keys()]}\nWrite (ask , del, add, average, quit): ').lower()
    except ValueError:
        print('Try again')
    else:
        if text == 'ask':
            name_friend = input('Write name:').upper()
            print(adress[name_friend])
        elif text == 'del':
            del_friend = input('Write name:').upper()
            del adress[del_friend]

        elif text == 'add':
            add_friend = input('New name: ')
            tell = int(input('Write telefone: '))
            friend_count = int(input('COunt of friend: '))
            adress[add_friend] = [tell, friend_count]
        elif text == 'average':
            sum_f = 0
            for count in adress:
                sum_f += adress[count][1]
            average = sum_f / len(adress)
            print(int(f'Average of friends: {average}'))
        elif text == 'quit':
            break
        else:
            print('Something went wrong. Try one more time.')

