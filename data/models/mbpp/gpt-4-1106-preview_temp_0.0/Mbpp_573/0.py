"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""


import numpy as np

def unique_product(lst):
    unique_elements = set(lst)
    product = np.prod(list(unique_elements))
    return product

assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000
