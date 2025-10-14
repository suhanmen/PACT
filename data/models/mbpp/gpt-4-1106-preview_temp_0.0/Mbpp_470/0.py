"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""



def add_pairwise(input_tuple):
    return tuple(input_tuple[i] + input_tuple[i+1] for i in range(len(input_tuple) - 1))

# Example usage
# result = add_pairwise((1, 5, 7, 8, 10))
# print(result)  # Output should be (6, 12, 15, 18)
