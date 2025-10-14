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
    lst_copy = lst.copy()  # create a copy of the original list to not modify it
    while lst_copy:
        sorted_lst.append(min(lst_copy))
        lst_copy.remove(min(lst_copy))
        if lst_copy:
            sorted_lst.append(max(lst_copy))
            lst_copy.remove(max(lst_copy))
    return sorted_lst
