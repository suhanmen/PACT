"""
Write a function to convert the given tuple to a key-value dictionary using adjacent elements. https://www.geeksforgeeks.org/python-convert-tuple-to-adjacent-pair-dictionary/
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
"""



def tuple_to_dict(tup):
    return {tup[i]: tup[i + 1] for i in range(0, len(tup), 2)}

# Example usage
# tuple_to_dict((1, 5, 7, 10, 13, 5))
