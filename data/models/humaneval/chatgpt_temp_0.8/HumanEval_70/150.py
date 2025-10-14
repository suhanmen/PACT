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

    # If the input list is empty, return an empty list
    if not lst:
        return result

    # Sort the list in ascending order
    sorted_lst = sorted(lst)

    # Initialize two pointers, one at the beginning and one at the end of the sorted list
    left = 0
    right = len(sorted_lst) - 1

    # While there are still elements in the sorted list
    while left <= right:

        # Add the minimum element to the result list
        result.append(sorted_lst[left])

        # If there are still elements left in the sorted list, add the maximum element to the result list
        if left != right:
            result.append(sorted_lst[right])

        # Move the pointers inward
        left += 1
        right -= 1

    return result
