'''program that count average temperature by user request'''

f = open('weather.log', 'r', encoding='utf-8')
t = f.readlines()
f.close()
count = s = 0
c_mounth = input(f'Choose a mounth:\n>')
for i in t:
	if i.split('-')[1] == c_mounth:
		temp_int = int(i.split()[2].replace('°C,',''))
		s += temp_int
		count += 1
if count == 0:
	print('We haven\'t this data.')
else:
	print(f'Averauge temp is: {(s / count):.1f}°C')

