"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""



def max_length(list_of_lists):
    max_len = 0
    max_list = []
    for lst in list_of_lists:
        if len(lst) > max_len:
            max_len = len(lst)
            max_list = lst
    return max_len, max_list


assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])
