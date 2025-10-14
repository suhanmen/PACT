def pluck(arr):
    even_nodes = [(index, node) for index, node in enumerate(arr) if node % 2 == 0]
    if not even_nodes:
        return []

    smallest_even_value = min(node for index, node in even_nodes)
    smallest_even_nodes = [(index, node) for index, node in even_nodes if node == smallest_even_value]
    return min(smallest_even_nodes)[::-1]
