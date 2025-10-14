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
    result = []
    while lst:
        # find the minimum value and remove it from the list
        min_val = min(lst)
        lst.remove(min_val)
        result.append(min_val)
        
        # if there are still values in the list, find the maximum
        if lst:
            max_val = max(lst)
            lst.remove(max_val)
            result.append(max_val)
    
    return result
