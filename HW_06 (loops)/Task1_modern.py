'''program that has some sentence (a string) on input
and returns a dict containing all unique words as keys and the number of occurrences as values

Version with random string maker and simple interface'''


import random


def string_randomizer(number: int, length: int):  # making a random string
    alph1 = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N'
        , 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    alph2 = ['A', 'E', 'I', 'O', 'U', 'Y']
    symb = ['', '', '', '', ',', '', '.', '.', '', '']

    string_all1 = ''
    for j in range(number):  # number of words
        string_word = ''
        for i in range(random.randint(1, length)):  # length of words
            rnd = [random.choice(alph1), random.choice(alph2)]  # choosing a type of letter
            string_word += random.choice(rnd)
        string_all1 += string_word + random.choice(symb) + ' '  # At the end conc. of random symbol
    return string_all1


string_all = input('Print your string, or press "Q" to choose random: ')  # dialogue with user

if string_all.lower() == 'q':
    while True:
        try:
            num_of_words = int(input('Choose number of words: '))
            len_of_words = int(input('Choose length of words: '))
        except ValueError:
            print('Try again')
        else:
            string_all = string_randomizer(num_of_words, len_of_words)  # this is our random string
            break

print(f'Your string is:\n {string_all}')
string_all = string_all.strip()      # making our string clear
string_all = string_all.replace(',', '')
string_all = string_all.replace('.', '')
list_of_keys = (string_all.split(' '))

dict_of_words = {}
for marker in list_of_keys:  # loop of keys
    if dict_of_words.get(marker, 0) != 0:  # take a value if dict have this key, and 0 if not
        dict_of_words[marker] += 1
    else:
        dict_of_words[marker] = 1

print(f'Here is Your dictionary:\n{dict_of_words}')

print('Here is the one more form:')
for pr_marker in set(sorted(dict_of_words.values())):  # loop in set of sorted values
    print(f'{pr_marker}: ', end='')
    for pr_d_marker in dict_of_words.keys():  # loop for choosing keys by values
        if dict_of_words.get(pr_d_marker) == pr_marker:
            print(f'"{pr_d_marker}"', end=' ')
    print()


