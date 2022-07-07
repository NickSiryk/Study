'''
A Python program to detect the number of local variables declared in a function.
'''

def f_test_1(n):
    return n

def f_test_2():
    a, b = 2, 8
    return a + b

def f_test_3(r, d):
    def f_test_3_1(a, b):
        c = 1
        return a + b + c
    f_test_3_1(r, d)

print(f_test_1.__code__.co_nlocals)
print(f_test_2.__code__.co_nlocals)
print(f_test_3.__code__.co_nlocals)