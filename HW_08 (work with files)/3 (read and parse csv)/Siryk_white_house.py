'''program that read a csv file and parse info from it

1. Who earns the least?
2. Who earns the most?
3. Average earnings of all employees.
4. Which 10 employees earn the most?
'''

f = open('white_house_2017_salaries_com.csv')
f.readline()
table = []
for i in f:
	info = i.split(';')
	info[2] = float((info[2]).replace('$', '').replace(',','').strip())
	info[0], info[1], info[2] = info[2], info[0], info[1]
	info[-1] = info[-1].strip()
	table.append(info)
f.close()

#1
table.sort()
for i in table:
	if i[0] > 0:
		print(f'{i[1]} has min salary ${i[0]}')
		break

#2
table.reverse()
print(f'{table[0][1]} has max salary ${table[0][0]}')

#3
all_sal = [s[0] for s in table]
print(f'Averauge salary is: ${(sum(all_sal) / len(all_sal)):.2f}')

#4
print('Top salaries is:')
for i in range(0,10):
	print(f'{i+1}. {table[i][1]} has salary ${table[i][0]}')
