'''
A Python program to access a function inside a function
'''

def f_test_1(r, d):
    n = 2

    def f_test_1_1(a):
        c = r + d
        return a + c
    if r >= d:
        return f_test_1_1
    else:
        return n


val_1 = f_test_1(1, 1)
val_2 = val_1(2)
print(val_2)

val_3 = f_test_1(1, 2)
print(val_3)