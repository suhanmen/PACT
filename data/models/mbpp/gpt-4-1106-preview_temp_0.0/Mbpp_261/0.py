"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""



def division_elements(tuple1, tuple2):
    try:
        return tuple(a / b for a, b in zip(tuple1, tuple2))
    except ZeroDivisionError:
        print('Error: Division by zero encountered.')
        return None

# Example usage
# result = division_elements((10, 4, 6, 9), (5, 2, 3, 3))
# print(result)  # Output should be (2.0, 2.0, 2.0, 3.0)
