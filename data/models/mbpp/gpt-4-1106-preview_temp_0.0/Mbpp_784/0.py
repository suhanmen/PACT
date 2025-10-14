"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""



def mul_even_odd(numbers):
    even = None
    odd = None
    for num in numbers:
        if even is None and num % 2 == 0:
            even = num
        if odd is None and num % 2 != 0:
            odd = num
        if even is not None and odd is not None:
            break
    return even * odd if even is not None and odd is not None else None

assert mul_even_odd([1,3,5,7,4,1,6,8]) == 4
