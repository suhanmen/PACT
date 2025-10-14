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
    # First, remove duplicates
    lst = list(set(lst))
    
    # If there are less than 2 elements, return None
    if len(lst) < 2:
        return None
    
    # Find the smallest element using min()
    smallest = min(lst)
    
    # Remove the smallest element from the list
    lst.remove(smallest)
    
    # Find the second smallest element using min()
    second_smallest = min(lst)
    
    return second_smallest
