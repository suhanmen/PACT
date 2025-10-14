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
    lst.sort() # sort the input list in ascending order
    
    while len(lst) > 0:
        result.append(lst.pop(0)) # add the minimum value to the result list
        if len(lst) > 0:
            result.append(lst.pop(-1)) # add the maximum value to the result list
    
    return result
