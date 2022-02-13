import time

name = 'Nick'
date = time.strftime('%A', time.localtime())

# 1st method (old)
print('Good day %s! %s is a perfect day to learn some python.' % (name, date))

# 2nd method (str.format)
print('Good day {}! {} is a perfect day to learn some python.'.format(name, date))

# 3rd method (f-string)
print(f'Good day {name}! {date} is a perfect day to learn some python.')

# 4th method (Template)
from string import Template
pr = 'Good day $name! $date is a perfect day to learn some python.'
pr = Template(pr).substitute(name=name, date=date)
print(pr)