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
    # If the list has 0 or 1 element, there is no 2nd smallest element
    if len(lst) < 2:
        return None
    
    # Convert the list to a set to remove duplicates
    unique_nums = set(lst)
    
    # If there are less than 2 unique elements, there is no 2nd smallest element
    if len(unique_nums) < 2:
        return None
    
    # Sort the unique elements in ascending order and return the 2nd element
    return sorted(unique_nums)[1]
