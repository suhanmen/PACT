"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""



def common_in_nested_lists(nested_lists):
    # Convert the first list to a set for intersection
    common_elements = set(nested_lists[0])
    # Perform intersection with all other lists
    for lst in nested_lists[1:]:
        common_elements.intersection_update(lst)
    return list(common_elements)

# Example usage
# common_elements = common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])
# print(common_elements)  # Output should be [12, 18] or [18, 12]
