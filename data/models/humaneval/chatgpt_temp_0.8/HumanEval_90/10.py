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
        return None # There are not enough elements to have a 2nd smallest
    else:
        unique_list = list(set(lst)) # Remove duplicates
        sorted_list = sorted(unique_list) # Sort
        if len(sorted_list) < 2:
            return None # There is no 2nd smallest
        else:
            return sorted_list[1] # Return the 2nd smallest
