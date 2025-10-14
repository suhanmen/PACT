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
    
    # sort the list and return the 2nd smallest element
    sorted_lst = sorted(set(lst)) # remove duplicates and sort
    if len(sorted_lst) == 1: # check if all elements are the same
        return None
    return sorted_lst[1]
