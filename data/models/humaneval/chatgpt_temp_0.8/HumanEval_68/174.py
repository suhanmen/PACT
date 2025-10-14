def pluck(arr):
    even_nodes = [(val, idx) for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_nodes:
        return []
    else:
        smallest_even = min(even_nodes)
        return [smallest_even[0], smallest_even[1]]
