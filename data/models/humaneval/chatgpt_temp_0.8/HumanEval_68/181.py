def pluck(arr):
    even_nodes = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_nodes.append([arr[i], i])

    if len(even_nodes) == 0:
        return []
    
    even_nodes.sort(key=lambda x: (x[0], x[1]))
    return even_nodes[0]
