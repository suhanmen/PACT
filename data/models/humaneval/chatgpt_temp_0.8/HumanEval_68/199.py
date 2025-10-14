def pluck(arr):
    even_values = [val for val in arr if val % 2 == 0]
    if not even_values:
        return []
    
    min_val = min(even_values)
    min_index = arr.index(min_val)
    return [min_val, min_index]
