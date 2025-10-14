"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""



def is_sublist(lst, sublst):
    it = iter(lst)
    return all(any(x == y for y in it) for x in sublst)

# Example usage
# assert is_sublist([2,4,3,5,7],[3,7])==False
