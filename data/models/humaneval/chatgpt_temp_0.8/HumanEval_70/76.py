def strange_sort_list(lst):
    # Check if the list is empty
    if not lst:
        return []

    # Initialize the result list and sort the input list
    result = []
    lst.sort()

    # Loop while the input list is not empty
    while lst:
        # Append the minimum value
        result.append(lst.pop(0))
        # If the input list is now empty, break out of the loop
        if not lst:
            break
        # Append the maximum value
        result.append(lst.pop())
    
    return result
