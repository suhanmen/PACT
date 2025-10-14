"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""



def diff_even_odd(numbers):
    first_even = None
    first_odd = None
    for num in numbers:
        if first_even is None and num % 2 == 0:
            first_even = num
        if first_odd is None and num % 2 != 0:
            first_odd = num
        if first_even is not None and first_odd is not None:
            break
    return first_even - first_odd if first_even is not None and first_odd is not None else None

assert diff_even_odd([1,3,5,7,4,1,6,8]) == 3
