def pluck(arr):
    even_vals = [num for num in arr if num % 2 == 0]
    if not even_vals:
        return []
    min_val = min(even_vals)
    min_index = arr.index(min_val)
    return [min_val, min_index]
