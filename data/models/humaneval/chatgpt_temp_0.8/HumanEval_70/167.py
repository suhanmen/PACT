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
    lst.sort() #sorts the input list in ascending order
    while lst:
        result.append(lst.pop(0)) #adds the minimum value to the result list
        if lst:
            result.append(lst.pop(-1)) #adds the maximum value to the result list
    return result
