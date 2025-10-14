def pluck(arr):
    even_nodes = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_nodes.append((arr[i], i))
    if not even_nodes:
        return []
    else:
        return min(even_nodes)
