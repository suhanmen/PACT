"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""



def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]

assert median_numbers(25,55,65)==55.0
