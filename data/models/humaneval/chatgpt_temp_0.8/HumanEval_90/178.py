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

    # If the list is empty or has only one element, return None
    if len(lst) < 2:
        return None

    sorted_lst = sorted(set(lst))  # Remove duplicates and sort the list

    # If the sorted list has less than 2 elements, return None
    if len(sorted_lst) < 2:
        return None

    return sorted_lst[1]  # Return the second smallest element
