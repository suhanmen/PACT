"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""



def tuple_str_int(tuple_str):
    # Remove the parentheses and split by comma
    tuple_str = tuple_str.strip('()')
    # Convert each number to an integer and create a tuple
    return tuple(map(int, tuple_str.split(', ')))

# Example usage
# assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
