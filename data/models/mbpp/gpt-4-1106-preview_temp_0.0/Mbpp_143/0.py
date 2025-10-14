"""
Write a function to find number of lists present in the given tuple.
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
"""



def find_lists(input_tuple):
    return sum(isinstance(item, list) for item in input_tuple)

assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
