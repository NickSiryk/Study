'''program that count average temperature by user request'''

import math
f = open('weather.log', 'r', encoding='utf-8')
t = f.readlines()
f.close()
s = 0
mounth = {(i.split('-')[1]) for i in t}	#set of mounths
c_mounth = input(f'choose mounth from this: {mounth}\n>>>')
s = [int(i.split()[2].replace('°C,','')) for i in t \
if i.split('-')[1] == c_mounth]
print(f'Averauge temp is: {(sum(s) / len(s)):.2f}°C')

