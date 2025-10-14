def pluck(arr):
    even_nodes = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_nodes.append((arr[i], i))
    if len(even_nodes) == 0:
        return []
    else:
        evens_sorted = sorted(even_nodes)
        return [evens_sorted[0][0], evens_sorted[0][1]]
