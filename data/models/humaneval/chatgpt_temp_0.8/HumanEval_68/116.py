def pluck(arr):
    even_vals = []
    for i, val in enumerate(arr):
        if val % 2 == 0:
            even_vals.append((val, i))
    if not even_vals:
        return []
    return min(even_vals)
