"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""



def check_smaller(first_tuple, second_tuple):
    return all(x > y for x, y in zip(first_tuple, second_tuple))

# Example usage
# assert check_smaller((1, 2, 3), (2, 3, 4)) == False
