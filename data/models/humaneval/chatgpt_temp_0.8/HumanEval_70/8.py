python
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

    result = []

    # Sort the list in ascending order
    lst.sort()

    # Use two pointers, one starting at the beginning of the list,
    # and the other starting at the end of the list
    left = 0
    right = len(lst) - 1

    while left <= right:
        # Append the left pointer to the result list
        result.append(lst[left])
        left += 1

        # If there are still elements in the list, append
        # the right pointer to the result list
        if left <= right:
            result.append(lst[right])
            right -= 1

    return result
