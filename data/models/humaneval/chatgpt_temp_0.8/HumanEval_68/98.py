def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.
    
    The plucked node should be returned in a list, [smallest_value, its_index].
    If there are no even values or the given array is empty, return [].
    """
    even_nodes = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_nodes.append((arr[i], i))
    if even_nodes:
        smallest_even = min(even_nodes, key=lambda x: (x[0], x[1]))
        return [smallest_even[0], smallest_even[1]]
    else:
        return []
