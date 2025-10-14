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
    if not lst:  # if the list is empty, return an empty list
        return []
    else:
        sorted_list = []  # create an empty list to store sorted integers
        while lst:  # while list is not empty
            sorted_list.append(min(lst))  # add the minimum value to sorted_list
            lst.remove(min(lst))  # remove the minimum value from lst
            if lst:  # if lst is not empty after removing minimum value
                sorted_list.append(max(lst))  # add the maximum value to sorted_list
                lst.remove(max(lst))  # remove the maximum value from lst
        return sorted_list
