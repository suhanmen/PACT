def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''

    sorted_lst = []

    # Keep looping while there are still elements in the list
    while lst:
        # Find the minimum value in the list
        min_val = min(lst)
        # Add it to the sorted list
        sorted_lst.append(min_val)
        # Remove it from the original list
        lst.remove(min_val)

        # If there are still elements in the list...
        if lst:
            # Find the maximum value in the list
            max_val = max(lst)
            # Add it to the sorted list
            sorted_lst.append(max_val)
            # Remove it from the original list
            lst.remove(max_val)

    # Return the sorted list
    return sorted_lst
