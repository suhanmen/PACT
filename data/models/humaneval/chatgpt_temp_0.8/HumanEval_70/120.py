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
    lst.sort() # Sort the list in ascending order
    while len(lst) > 0:
        sorted_lst.append(lst.pop(0)) # Add the smallest value
        if len(lst) > 0:
            sorted_lst.append(lst.pop(-1)) # Add the largest value
    return sorted_lst
