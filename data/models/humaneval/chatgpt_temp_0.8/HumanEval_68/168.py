def pluck(arr):
    even_vals = [val for val in arr if val % 2 == 0]
    if not even_vals:
        return []
    min_even_val = min(even_vals)
    min_even_val_indices = [i for i, val in enumerate(arr) if val == min_even_val]
    return [min_even_val, min(min_even_val_indices)]
