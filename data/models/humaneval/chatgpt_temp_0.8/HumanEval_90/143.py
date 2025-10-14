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

    # Ensure there are at least 2 elements in the list
    if len(lst) < 2:
        return None

    # Sort the list in ascending order
    sorted_lst = sorted(set(lst))

    # Return the second smallest element if it exists, otherwise return None
    if len(sorted_lst) > 1:
        return sorted_lst[1]
    else:
        return None
