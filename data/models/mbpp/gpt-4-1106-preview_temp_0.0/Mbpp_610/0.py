"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""



def remove_kth_element(lst, k):
    # Copy the list to avoid modifying the original list
    new_lst = lst[:]
    # Remove the k'th element
    del new_lst[k]
    return new_lst

# Example usage
# assert remove_kth_element([1,1,2,3,4,4,5,1], 3) == [1, 1, 3, 4, 4, 5, 1]
