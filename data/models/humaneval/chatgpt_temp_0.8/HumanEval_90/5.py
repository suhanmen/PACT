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
    if len(lst) < 2:
        # There is no 2nd smallest element
        return None
    # Sort the list in ascending order
    sorted_lst = sorted(set(lst))
    # If there are fewer than two distinct elements, there is no 2nd smallest element
    if len(sorted_lst) < 2:
        return None
    # Return the 2nd smallest element
    return sorted_lst[1]
