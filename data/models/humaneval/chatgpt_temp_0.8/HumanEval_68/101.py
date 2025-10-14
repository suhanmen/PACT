def pluck(arr):
    min_even = float('inf')
    min_even_index = None
    for i, val in enumerate(arr):
        if val % 2 == 0 and val < min_even:
            min_even = val
            min_even_index = i
    if min_even_index is not None:
        return [min_even, min_even_index]
    else:
        return []
