"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""



def is_product_even(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product % 2 == 0

assert is_product_even([1,2,3])
