"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""



def tuple_to_int(t):
    return int(''.join(map(str, t)))

# Example usage
# assert tuple_to_int((1,2,3)) == 123
