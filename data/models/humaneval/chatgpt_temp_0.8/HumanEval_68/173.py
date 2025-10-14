def pluck(arr):
    even_values = [n for n in arr if n % 2 == 0]
    if not even_values:
        return []
    min_even = min(even_values)
    min_even_idx = arr.index(min_even)
    return [min_even, min_even_idx]
