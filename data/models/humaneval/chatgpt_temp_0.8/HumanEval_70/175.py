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
    sorted_list = []
    while lst:
        minimum = min(lst)
        maximum = max(lst)
        sorted_list.append(minimum)
        if minimum != maximum:
            sorted_list.append(maximum)
        lst.remove(minimum)
        if minimum != maximum:
            lst.remove(maximum)
    return sorted_list
