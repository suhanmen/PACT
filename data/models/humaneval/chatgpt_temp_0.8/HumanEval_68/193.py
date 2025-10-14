def pluck(arr):
    even_nodes = [(val, i) for i, val in enumerate(arr) if val % 2 == 0]
    if not even_nodes:
        return []

    smallest_val, smallest_idx = even_nodes[0]
    for val, i in even_nodes:
        if val < smallest_val:
            smallest_val = val
            smallest_idx = i

    return [smallest_val, smallest_idx]
