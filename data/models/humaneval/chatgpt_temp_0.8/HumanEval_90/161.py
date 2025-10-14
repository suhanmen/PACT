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
    if len(lst) < 2: # check if there is no 2nd smallest element
        return None
    else:
        unique_lst = list(set(lst)) # remove duplicates
        if len(unique_lst) < 2: # check if there is no 2nd unique element
            return None
        else:
            sorted_lst = sorted(unique_lst) # sort in ascending order
            return sorted_lst[1] # return 2nd element
