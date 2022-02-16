name = input('Tell me your name: ')
while True:
    age = input('Tell me your age: ').strip()
    if age.isdigit():
        age = int(age)
        break
    else:
        print('Something went wrong. Try one more time.')

print(f'Hello {name}! On your next birthday you\'ll be {age + 1} years!')

