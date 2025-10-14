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
    lst_sorted = sorted(lst) # First sort the list in ascending order
    while lst_sorted:
        result.append(lst_sorted.pop(0)) # Add the minimum value to the result list
        if lst_sorted:
            result.append(lst_sorted.pop(-1)) # Add the maximum remaining value to the result list
    return result
