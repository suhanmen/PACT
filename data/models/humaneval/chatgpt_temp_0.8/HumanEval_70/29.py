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
    lst_len = len(lst)

    for i in range(lst_len):
        if i % 2 == 0:
            sorted_lst.append(min(lst))
            lst.remove(min(lst))
        else:
            sorted_lst.append(max(lst))
            lst.remove(max(lst))

        if not lst:
            break

    return sorted_lst
