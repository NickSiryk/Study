'''
SQL queries:
1.1 Average earnings of all employees.
1.2 Which 10 employees earn the most.
1.3 How many people are temporarily assigned to another position?
1.4. How many people are in the position "STAFF ASSISTANT"
1.5. The average salary of all "STAFF ASSISTANT"
1.6. How many positions and what are they.
1.7. How many people are in each position.
'''
import sqlite3

con = sqlite3.connect('wh.db')

cur = con.cursor()

def task_1_1(cur_f):
    aver = cur_f.execute('''SELECT sum(salary)/count(name)
                           AS middle
                           FROM sotr;''')
    return aver.fetchone()


def task_1_2(cur_f):
    lst = cur_f.execute('''SELECT name, salary 
                        FROM sotr 
                        ORDER BY salary 
                        DESC LIMIT 10;''')
    return lst.fetchall()


def task_1_3(cur_f):
    lst = cur_f.execute('''SELECT status, count(status) 
                        FROM sotr 
                        WHERE status='Detailee';''')
    return lst.fetchall()


def task_1_4(cur_f):
    aver = cur_f.execute('''SELECT position_title, count(position_title) 
                            FROM sotr 
                            WHERE position_title='STAFF ASSISTANT';''')
    return aver.fetchone()


def task_1_5(cur_f):
    aver = cur_f.execute('''SELECT position_title, sum(salary)/count(position_title)
                            AS miidle 
                            FROM sotr 
                            WHERE position_title='STAFF ASSISTANT';''')
    return aver.fetchone()

def task_1_6(cur_f):
    lst = cur_f.execute('''SELECT position_title
                        FROM sotr
                        GROUP BY position_title;''')
    return lst.fetchall()


def task_1_7(cur_f):
    lst = cur_f.execute('''SELECT position_title, count(name) as count 
                        FROM sotr 
                        GROUP BY position_title 
                        ORDER BY count 
                        DESC;''')
    return lst.fetchall()

print('task 1.1:\n', task_1_1(cur))
print('task 1.2:\n', task_1_2(cur))
print('task 1.3:\n', task_1_3(cur))
print('task 1.4:\n', task_1_4(cur))
print('task 1.5:\n', task_1_5(cur))
print('task 1.6:\n', task_1_6(cur))
print('task 1.7:\n', task_1_7(cur))

con.close()
