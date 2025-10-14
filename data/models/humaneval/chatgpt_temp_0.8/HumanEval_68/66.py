python
def pluck(arr):
    even_nodes = [(val, idx) for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_nodes:
        return []
    else:
        smallest_even_node = min(even_nodes, key=lambda x: (x[0], x[1]))
        return list(smallest_even_node)
