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
    lst.sort()  # sort the input list in ascending order
    
    while len(lst) > 0:
        # Add the smallest value to the sorted list
        sorted_lst.append(lst.pop(0))
        
        if len(lst) > 0:
            # Add the largest value to the sorted list
            sorted_lst.append(lst.pop())
    
    return sorted_lst
