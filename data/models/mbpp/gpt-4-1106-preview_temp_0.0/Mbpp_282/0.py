"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""


def sub_list(list1, list2):
    return [a - b for a, b in zip(list1, list2)]

# Example usage
# assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
