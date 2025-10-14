"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""



def count_element_in_list(list_of_lists, element):
    return sum(element in sublist for sublist in list_of_lists)

# Example usage:
# assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1) == 3
