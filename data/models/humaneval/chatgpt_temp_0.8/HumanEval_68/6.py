def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node
    that has smallest index.
    The plucked node should be returned in a list, [ smallest_value, its index ].
    If there are no even values or the given array is empty, return [].
    """
    
    # Initialize variables to hold the minimum even value and its index
    min_even_val = float('inf')
    min_even_idx = float('inf')
    
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < min_even_val:
            # Update minimum even value and its index
            min_even_val = arr[i]
            min_even_idx = i
    
    # Check if a minimum even value was found
    if min_even_val == float('inf'):
        return []
    else:
        return [min_even_val, min_even
