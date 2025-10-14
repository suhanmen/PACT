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
    # Check if list is empty or has only one element
    if len(lst) < 2:
        return None
    
    # Remove duplicates from the list and sort it in ascending order
    unique_lst = list(set(lst))
    unique_lst.sort()
    
    # Check if there is a second smallest element
    if len(unique_lst) < 2:
        return None
    
    # Return the second smallest element
    return unique_lst[1]
