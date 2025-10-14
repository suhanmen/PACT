def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes, 
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node 
    that has smallest index.
    The plucked node should be returned in a list, [smallest_value, its_index].
    If there are no even values or the given array is empty, return [].
    """

    # Check if the array is empty
    if len(arr) == 0:
        return []

    # Initialize variables to keep track of the smallest even value and its index
    smallest_even_value = float('inf')
    smallest_even_value_index = float('inf')

    # Loop through the array and find the smallest even value and its index
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_even_value:
            smallest_even_value = arr[i]
            smallest_even_value_index = i

    # I
