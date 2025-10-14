import math

def multiply_num(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product / len(numbers)

assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)