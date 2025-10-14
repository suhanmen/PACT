"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""



def find_dissimilar(tuple1, tuple2):
    return tuple(set(tuple1) ^ set(tuple2))

# Example usage
# dissimilar_elements = find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10))
# print(dissimilar_elements)
