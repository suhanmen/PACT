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
    # If the list is empty or contains only one element, there is no 2nd smallest element
    if len(lst) < 2:
        return None
    
    # Sort the list in ascending order
    sorted_lst = sorted(lst)
    
    # Find the 2nd smallest element in the sorted list
    second_smallest = sorted_lst[1]
    
    # If the 2nd smallest element is the same as the smallest element, there is no 2nd smallest element
    if second_smallest == sorted_lst[0]:
        return None
    
    return second_smallest
