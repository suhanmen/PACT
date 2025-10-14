def pluck(arr):
    even_nodes = []
    for i, node in enumerate(arr):
        if node % 2 == 0:
            even_nodes.append((node, i))
    if not even_nodes:
        return []
    else:
        even_nodes.sort()
        return [even_nodes[0][0], even_nodes[0][1]]
