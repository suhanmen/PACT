"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""



def number_ctr(input_string):
    return sum(c.isdigit() for c in input_string)

assert number_ctr('program2bedone') == 1
