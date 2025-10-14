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
    # Remove duplicates
    lst = list(set(lst))

    # If there are less than 2 elements, return None
    if len(lst) < 2:
        return None
    
    # Sort the list and return the second element
    lst.sort()
    return lst[1]
