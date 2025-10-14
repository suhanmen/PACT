def strange_sort_list(lst):

    # Base case: return an empty list if given list is empty
    if not lst:
        return []

    # Initialize variables
    min_val = min(lst)
    max_val = max(lst)
    result = [min_val, max_val]

    # Loop through remaining values
    for i in range(len(lst)-2):
        if i % 2 == 0:
            # If i is even, add the minimum value to result
            lst.remove(min_val)
            min_val = min(lst)
            result.append(min_val)
        else:
            # If i is odd, add the maximum value to result
            lst.remove(max_val)
            max_val = max(lst)
            result.append(max_val)

    return result
