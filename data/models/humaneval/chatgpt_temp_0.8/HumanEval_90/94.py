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
    # Sort the list in ascending order
    lst = sorted(lst)
    
    # If the list has less than 2 elements, return None
    if len(lst) < 2:
        return None
    
    # Iterate through the list, skipping repeated elements
    count = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            count += 1
            if count == 2:
                return lst[i]
    
    # If we haven't found the 2nd smallest element by now, it doesn't exist
    return None
