def pluck(arr):
    even_nodes = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_nodes.append((arr[i], i))
    if not even_nodes:
        return []
    smallest_even_node = min(even_nodes, key=lambda x: (x[0], x[1]))
    return [smallest_even_node[0], smallest_even_node[1]]
