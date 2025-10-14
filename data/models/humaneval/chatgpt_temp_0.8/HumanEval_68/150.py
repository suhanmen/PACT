def pluck(arr):
    even_nodes = [(i, node) for i, node in enumerate(arr) if node % 2 == 0]
    if not even_nodes:
        return []
    else:
        smallest_even_node = min(even_nodes, key=lambda x: (x[1], x[0]))
        return [smallest_even_node[1], smallest_even_node[0]]
