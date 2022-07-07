'''Task:

Generate 2 lists with the length of 10 with random integers from 1 to 10,
make a third list containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
'''

import random

count = 0
my_list1 = []  # empty list1
my_list2 = []  # empty list2
while count < 10:
    my_list1 += [random.randint(1, 10)]  # conc of lists1
    my_list2 += [random.randint(1, 10)]  # conc of lists2
    count += 1
print('1st list: ', my_list1)
print('2nd list: ', my_list2)
my_set1 = set(my_list1)  # transform to set
my_set2 = set(my_list2)  # transform to set
sum_list = list(my_set1 & my_set2)  # set Intersection and back to list
print('Intersection list: ', sum_list)
