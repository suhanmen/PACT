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
    if len(lst) < 2:  # If the list has less than 2 elements, return None.
        return None
    
    # Sort the list in ascending order and retrieve the 2nd element.
    second_smallest = sorted(lst)[1]
    
    # If the 2nd smallest element is the same as the smallest element, return None.
    if second_smallest == sorted(lst)[0]:
        return None
    
    return second_smallest
