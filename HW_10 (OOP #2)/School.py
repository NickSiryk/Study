'''
Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one called Teacher. 
'''

class Person:
    def __init__(self, last_name, name, pfath, p_type):
        self.name = name
        self.last_name = last_name
        self.pfath = pfath
        self.p_type = p_type

    def change_name(self, info_new):
        self.name = info_new

    def change_last_name(self, info_new):
        self.last_name = info_new

    def change_pfath(self, info_new):
        self.pfath = info_new

    def inform(self):
        print(f'This is {self.last_name} {self.name} {self.pfath}. This Person is {self.p_type}')


class Student(Person):
    def __init__(self, name, last_name, pfath, class_num):
        self.class_num = class_num
        Person.__init__(self, name, last_name, pfath, p_type='Student')

    def change_dinf(self, info_new):
        self.class_num = info_new

    def deep_info(self):
        '''
        :return: more info about object
        '''
        self.inform()
        print(f'Studying in {self.class_num} class.')


class Teacher(Person):
    def __init__(self, name, last_name, pfath, sallary = 0):
        self.sallary = sallary
        Person.__init__(self, name, last_name, pfath, p_type='Teacher')

    def change_dinf(self, info_new):
        self.sallary = info_new

    def deep_info(self):
        '''
        :return: more info about object
        '''
        self.inform()
        print(f'Salary is ${self.sallary}.')


p1 = Student('Ivanov', 'Artur', 'Petrovuch', 8)
p2 = Student('Petrov', 'Ivan', 'Mykhailovuch', 7)
p1.deep_info()
p2.deep_info()
p2.change_dinf(8)
p2.deep_info()

t1 = Teacher('Bond', 'James', 'Jn', 1000)
t2 = Teacher('Bond', 'Dan', '', 1700)
t1.deep_info()
t2.deep_info()
t2.change_dinf(1500)
t2.deep_info()


p1.change_name('PEDRO')
p2.change_name('PEDRO')
t1.change_name('PEDRO')
t2.change_name('PEDRO')

p1.inform()
p2.inform()
t1.inform()
t2.inform()
