"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""



def cube_sum(n):
    even_sum = 0
    for i in range(1, n+1):
        even_sum += (2 * i) ** 3
    return even_sum

assert cube_sum(2) == 72
