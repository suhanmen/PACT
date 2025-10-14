def pluck(arr):
    even_nodes = [(node, index) for index, node in enumerate(arr) if node % 2 == 0]
    if not even_nodes:
        return []
    else:
        smallest = min(even_nodes, key=lambda x: (x[0], x[1]))
        return [smallest[0], smallest[1]]
