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
    result = []  # create an empty list to store the sorted values
    lst.sort()  # sort the input list in ascending order
    while lst:
        # pop the first and last elements of the list and append them to the result
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop(-1))
    return result
