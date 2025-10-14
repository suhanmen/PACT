def pluck(arr):
    even_nodes = []
    for i, val in enumerate(arr):
        if val % 2 == 0:
            even_nodes.append((val, i))
    if not even_nodes:
        return []
    smallest_even_value = min(even_nodes)[0]
    smallest_even_nodes = [node for node in even_nodes if node[0] == smallest_even_value]
    return min(smallest_even_nodes, key=lambda x: x[1])
