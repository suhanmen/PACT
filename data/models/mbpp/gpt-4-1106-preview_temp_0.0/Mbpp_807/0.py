"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""



def first_odd(numbers):
    for num in numbers:
        if num % 2 != 0:
            return num
    return None  # In case there are no odd numbers

assert first_odd([1,3,5]) == 1
