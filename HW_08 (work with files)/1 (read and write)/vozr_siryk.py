'''program that read info from file'''

info = open('fio_siryk.txt')
work_info = info.readlines()
info.close()
name = work_info[0].split(' ')[1]
age = int(work_info[1].split('-')[-1])
print(f'Hello, {name}! Your age is {2022 - age} years!')
