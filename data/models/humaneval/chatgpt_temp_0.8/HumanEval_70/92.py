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

    # Create an empty list to store the result
    result = []
    
    # Sort the input list in ascending order
    lst.sort()
    
    # Loop through the sorted input list, adding the smallest and largest
    # remaining values to the result list in alternating order
    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop(-1))
    
    return result
