def strange_sort_list(lst):
    result = []  # Initialize an empty list to store the sorted order
    lst.sort()  # Sort the input list in ascending order
    while lst:  # Continue until the input list is empty
        result.append(lst.pop(0))  # Add the minimum value to the result list and remove it from input list
        if lst:  # If input list is not empty, add the maximum value to the result list and remove it from input list
            result.append(lst.pop())
    return result
