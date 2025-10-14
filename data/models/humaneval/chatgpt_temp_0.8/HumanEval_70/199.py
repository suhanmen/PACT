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
    lst = sorted(lst)
    left_idx, right_idx = 0, len(lst) - 1
    while left_idx <= right_idx:
        if left_idx == right_idx:
            sorted_lst.append(lst[left_idx])
            break
        sorted_lst.append(lst[left_idx])
        sorted_lst.append(lst[right_idx])
        left_idx += 1
        right_idx -= 1
    return sorted_lst
