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

    # sort the list in ascending order
    lst.sort()

    # create two variables to keep track of the start and end of the list
    start = 0
    end = len(lst) - 1

    # create a new list to store the strange order
    strange_order = []

    # loop through the list
    while start <= end:
        # add the minimum value to the strange order list
        strange_order.append(lst[start])
        # increment the start variable
        start += 1

        # check if there are still items in the list
        if start <= end:
            # add the maximum value to the strange order list
            strange_order.append(lst[end])
            # decrement the end variable
            end -= 1

    return strange_order
