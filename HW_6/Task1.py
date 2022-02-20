string_all = input('Print your string: ')  # dialogue with user

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
