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
    if len(lst) < 2:  # Check if the list has less than 2 elements
        return None
    else:
        unique_nums = sorted(set(lst))  # Remove duplicates and sort the list
        if len(unique_nums) < 2:  # Check if there is only one unique number in the list
            return None
        else:
            return unique_nums[1]  # Return the second smallest number
