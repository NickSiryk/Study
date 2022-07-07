class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = int(age)

    def human_age(self):
        '''
        takes values for a dog’s age
        :return: the dog’s age in human equivalent.
        '''
        print(f'Human equivalent is {self.age_factor * self.age} years old')


info_age = input('Print a dog\'s age, please: ')
first = Dog(info_age)
first.human_age()