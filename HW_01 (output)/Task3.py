'''Write a program, which has two print statements to print the following text
(capital letters “O” and “H”, made from “#” symbols):
#########
#       #
#       #
#       #
#########

#       #
#       #
#########
#       #
#       #
Pay attention that usage of spaces is forbidden,
as well as creating the whole result text string using “”” ”””, use ‘\n’ and ‘\t’ symbols instead.'''

print('#'*9+'\n#', '#\n#', '#\n#', '#\n'+'#'*9, sep='\t\t', end='\n\n')
print('#', '#\n#', '#\n'+'#'*9+'\n#', '#\n#', '#', sep='\t\t')
