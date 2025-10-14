def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.

    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    if len(lst) < 2: # check if the list has at least 2 elements
        return None
    
    # find the 2nd smallest element using sorting
    sorted_lst = sorted(set(lst)) # remove duplicates and sort the list
    if len(sorted_lst) < 2: # check if there is no 2nd element
        return None
    return sorted_lst[1]
