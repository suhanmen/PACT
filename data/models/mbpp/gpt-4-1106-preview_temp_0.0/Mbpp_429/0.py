"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""



def and_tuples(tuple1, tuple2):
    return tuple(a & b for a, b in zip(tuple1, tuple2))

# Example usage
# result = and_tuples((10, 4, 6, 9), (5, 2, 3, 3))
# print(result)  # Output should be (0, 0, 2, 1)
