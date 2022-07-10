'''
program that read a csv file and parse info from it using OOP
'''

class Employee:

    count = 0   # count of class objects
    staff = 0   # count employees who work full-time (not 'Detailee')
    all_salary = 0  # variable to the class, which will automatically sum the salaries of all employees

    def __init__(self, line_dict: dict):
        self.name = line_dict['NAME']
        self.status = line_dict['STATUS']
        self.salary = line_dict['SALARY']
        self.pay_basis = line_dict['PAY BASIS']
        self.position_title = line_dict['POSITION TITLE']
        self.__class__.count += 1

    def __str__(self):
        return f'{self.name} as {self.position_title}'

    def __repr__(self):
        return f'{self.name} as {self.position_title} with salary ${self.salary}'

    def __setattr__(self, key, value):
        '''
        Recalculation of common variables when changing an attribute
        '''
        if key == 'status':
            try:
                if getattr(self, key) == 'Detailee' and value != 'Detailee':
                    self.__class__.staff += 1
                elif getattr(self, key) != 'Detailee' and value == 'Detailee':
                    self.__class__.staff -= 1
            except AttributeError:
                if value != 'Detailee':
                    self.__class__.staff += 1

        # Recalculation sum the salaries of all employees
        if key == 'salary':
            try:
                self.__class__.all_salary -= getattr(self, key)
                self.__class__.all_salary += value
            except AttributeError:
                self.__class__.all_salary += value
        self.__dict__[key] = value

    def __del__(self):
        '''
        Recalculation of common variables when object deletes
        '''
        if self.status != 'Detailee':
            self.__class__.staff -= 1
        self.__class__.count -= 1
        self.__class__.all_salary -= self.salary

    @classmethod
    def report(cls):
        print(f'Count of employees: {cls.count}'
              f'Sum the salaries of all employees: ${cls.all_salary}'
              f'Average salary is: ${(cls.all_salary/cls.count):.2f}')

class WH:
    '''
    Class that processes the file, creates a database and allows you to work with it
    '''
    def __init__(self, database):
        self.sotr_list = []
        self.get_sotr(database)

    def get_sotr(self, database):
        '''
        opens a file with info and creates a list of employee objects at the start
        '''

        f = open(database)
        self.database = f.readlines()
        f.close()

        # makes a dict keys
        head = self.database[0].split(';')
        head = [h.strip() for h in head]
        temp_dict = {}

        for i in self.database[1:]:
            s = i.strip().split(';')
            for n, j in enumerate(head):
                if j == 'SALARY':
                    # convert salary type from str to float
                    temp_dict[j] = float(s[n].replace('$', '').replace(',', ''))
                else:
                    temp_dict[j] = s[n]
            # creates an object of class Employee
            emp = Employee(temp_dict)
            self.sotr_list.append(emp)

    def mid_salary(self, pos=''):
        '''
        :param pos: position to calculate, or 'empty' to calculate all
        :return: the Average earnings of all employees or employees by position
        '''
        if pos == '':
            answer = sum([sal.salary for sal in self.sotr_list])/len(self.sotr_list)
            return "%.2f" % answer
        else:
            temp_tuple = tuple(filter(lambda i: i.position_title == pos, self.sotr_list))
            # check if position exist
            if len(temp_tuple) == 0:
                return f'No position {pos}!'
            else:
                answer = sum([sal.salary for sal in temp_tuple]) / len(temp_tuple)
                return "%.2f" % answer

    def top_10(self):
        '''
        :return: Which 10 employees earn the most
        '''
        answer_list = {}
        temp_list = sorted(self.sotr_list, key=lambda i: i.salary, reverse=True)
        for i in range(10):
            answer_list[i+1] = temp_list[i]
        return answer_list

    def Detailee_staff(self):
        '''
        :return: number of employees with "Detailee" status
        '''
        answer = len(tuple(filter(lambda i: i.status == 'Detailee', self.sotr_list)))
        return f'{answer} peoples has status: "Detailee"'

    def num_by_pos(self, pos):
        '''
        :param pos: position to filter
        :return: number of employees on position "pos"
        '''
        answer = len(tuple(filter(lambda i: i.position_title == pos, self.sotr_list)))
        return f'{answer} peoples has position: {pos}'

    def all_pos(self):
        '''
        :return: number of different positions
        '''
        answer = set((i.position_title for i in self.sotr_list))
        num = len(answer)
        print(f'We have {num} different positions:')
        print(answer)

    def num_of_pos(self):
        '''
        :return: dict of positions as keys and number of employees on position as value
        '''
        temp_set = set((i.position_title for i in self.sotr_list))
        answer = {}
        for n in temp_set:
            answer[n] = len(tuple(filter(lambda i: i.position_title == n, self.sotr_list)))
        return answer

    def recount(self):
        '''
        Recalculation sum the salaries of all employees
        '''
        su = 0
        for s in self.sotr_list:
            su += s.salary
        s.__class__.all_salary = su

    @staticmethod
    def sum_salary(*args, args_list=''):
        if args_list != '':
            return sum(i.salary for i in args_list)
        else:
            return sum(i.salary for i in args)

    @staticmethod
    def avg_salary(*args, args_list=''):
        if args_list != '':
            a = tuple(i.salary for i in args_list)
        else:
            a = tuple(i.salary for i in args)
        return round((sum(a) / len(a)), 2)


w = WH('white_house_2017_salaries_com.csv')

print(f'Middle salary is ${w.mid_salary()}')
print(w.top_10())
print(w.Detailee_staff())

print(w.num_by_pos('STAFF ASSISTANT'))
print(w.num_by_pos('RESEARCH ASSOCIATE'))

print(f"Middle salary of STAFF ASSISTANT is ${w.mid_salary('STAFF ASSISTANT')}")
w.all_pos()
print(w.num_of_pos())

print(Employee.count)
print(Employee.staff)
w.sotr_list[57].status = 'Employee'
print(Employee.staff)

print(Employee.all_salary)
w.sotr_list[57].salary = 200000
print(Employee.all_salary)

print(w.sotr_list[57])
del w.sotr_list[57]
print(w.sotr_list[57])

print(Employee.staff)
print(Employee.all_salary)

print(w.sum_salary(w.sotr_list[1], w.sotr_list[10], w.sotr_list[100]))
print(w.avg_salary(w.sotr_list[1], w.sotr_list[10], w.sotr_list[100]))


