'''
   A simple greeting program
'''

class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def talk(self):
        '''
        :return: a greeting from the person containing
        '''
        print(f'Hello, my name is {self.name} {self.last_name} and I’m {self.age} years old')


info_name = input('Print Your name, please: ').strip()
info_l_n = input('Print Your last name, please: ').strip()
info_age = input('Print Your age, please: ').strip()

first = Person(info_name, info_l_n, info_age)

first.talk()
