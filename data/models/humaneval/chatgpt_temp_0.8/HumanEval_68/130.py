def pluck(arr):
    even_nodes = [node for node in arr if node % 2 == 0]
    
    if not even_nodes:
        return []
    
    smallest_even = min(even_nodes)
    smallest_even_index = arr.index(smallest_even)
    
    return [smallest_even, smallest_even_index]
