python
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
    # Remove duplicates from the list
    lst = list(set(lst))
    
    # If there are less than two elements in the list, return None
    if len(lst) < 2:
        return None
    
    # Find the second smallest element in the list
    smallest = min(lst)
    second_smallest = None
    for num in lst:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
            
    return second_smallest
