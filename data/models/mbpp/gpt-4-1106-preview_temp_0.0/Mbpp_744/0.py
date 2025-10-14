"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""



def check_none(input_tuple):
    return any(item is None for item in input_tuple)

# Example usage
# assert check_none((10, 4, 5, 6, None)) == True
