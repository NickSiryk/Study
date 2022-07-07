def choose_func(list, func1, func2):
    '''
    A function which takes a list of nums and 2 callback functions.
    If all nums inside the list are positive, execute the first function on that list and return the result of it.
    Otherwise, return the result of the second one

    :param list: list of nums
    :param func1: callback function #1
    :param func2: callback function #2
    '''
    index = min(list)
    if index < 0:
        return func2(list)
    else:
        return func1(list)


# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]