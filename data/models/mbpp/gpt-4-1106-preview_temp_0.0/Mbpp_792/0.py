"""
Write a python function to count the number of lists in a given number of lists.
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
"""



def count_list(list_of_lists):
    """
    This function counts the number of lists within a list.

    :param list_of_lists: List containing other lists
    :return: The count of lists within the given list
    """
    return len(list_of_lists)

# Example usage:
# assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
