def pluck(arr):
    even_nodes = [(index, node) for index, node in enumerate(arr) if node % 2 == 0]
    if not even_nodes:
        return []
    smallest_even_value = min(even_nodes, key=lambda x: x[1])[1]
    smallest_node_with_smallest_even_value = min((node for node in even_nodes if node[1] == smallest_even_value), key=lambda x: x[0])
    return [smallest_even_value, smallest_node_with_smallest_even_value[0]]
