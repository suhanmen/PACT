"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""



def max_sum_list(list_of_lists):
    return max(list_of_lists, key=sum)


assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]) == [10, 11, 12]
