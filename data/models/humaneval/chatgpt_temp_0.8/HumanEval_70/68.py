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
    lst.sort()

    for i in range(lst_len // 2):
        sorted_lst.append(lst[i])
        sorted_lst.append(lst[lst_len - i - 1])

    if lst_len % 2 == 1:
        sorted_lst.append(lst[lst_len // 2])

    return sorted_lst
