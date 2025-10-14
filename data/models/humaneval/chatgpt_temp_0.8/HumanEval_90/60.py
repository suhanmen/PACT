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
        return None
    else:
        # First we need to remove duplicates
        lst = list(set(lst))
        # Then we sort the list in ascending order
        lst.sort()
        # If there is a second smallest element, return it
        if len(lst) > 1:
            return lst[1]
        # Otherwise, return None
        else:
            return None
