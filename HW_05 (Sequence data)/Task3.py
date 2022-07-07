'''program that find all integers from the list that are
divisible by 7 but not a multiple of 5, and store them in a separate list'''

num_list = []  # create empty list
num_list.extend(range(1, 101))  # add numbers in list

i = 0  # create a counter
final_list = []  # create empty list

while i < len(num_list):
    if num_list[i] % 7 == 0 and not num_list[i]/7 % 5 == 0:  # our logic
        final_list += [num_list[i]]  # conc of final list and items
    i += 1

print(final_list)
