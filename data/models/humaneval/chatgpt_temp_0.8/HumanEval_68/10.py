python
def pluck(arr):
    even_vals = [val for val in arr if val % 2 == 0]
    if not even_vals:
        return []
    min_val = min(even_vals)
    min_index = arr.index(min_val)
    return [min_val, min_index]
