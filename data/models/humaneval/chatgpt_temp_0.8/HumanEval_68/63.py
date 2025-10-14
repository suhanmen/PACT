def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes, 
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has smallest index.
    The plucked node should be returned in a list, [ smallest_value, its index ],
    If there are no even values or the given array is empty, return [].
    """
    smallest_value = float("inf")
    smallest_index = float("inf")
    for i, val in enumerate(arr):
        if val % 2 == 0 and val < smallest_value:
            smallest_value = val
            smallest_index = i
        elif val % 2 == 0 and val == smallest_value and i < smallest_index:
            smallest_index = i
    if smallest_value == float("inf"):
        return []
    return [smallest_value, smallest_index]
