"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""



def union_elements(tuple1, tuple2):
    # Combine the tuples and convert to a set to remove duplicates
    union_set = set(tuple1) | set(tuple2)
    # Convert the set back to a tuple and sort it
    sorted_tuple = tuple(sorted(union_set))
    return sorted_tuple

# Example usage
# assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
