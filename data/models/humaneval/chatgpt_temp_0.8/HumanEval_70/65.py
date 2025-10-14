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

    # Sort the given list in ascending order
    lst.sort()

    # Initialize two pointers
    left = 0
    right = len(lst) - 1

    # Initialize an empty result list
    result = []

    # Loop through the list until both pointers meet
    while left <= right:
        # Append the minimum value to the result list
        result.append(lst[left])

        # If there are more than one elements remaining
        if left != right:
            # Append the maximum value to the result list
            result.append(lst[right])

        # Increment the left pointer
        left += 1

        # Decrement the right pointer
        right -= 1

    return result
