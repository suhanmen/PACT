"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""



def is_divisible_by_11(number):
    return number % 11 == 0

assert is_divisible_by_11(12345) == False
