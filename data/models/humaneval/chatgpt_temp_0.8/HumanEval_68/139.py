python
def pluck(arr):
    even_values = [n for n in arr if n % 2 == 0]
    if not even_values:
        return []
    smallest_even_value = min(even_values)
    smallest_indexes = [i for i, n in enumerate(arr) if n == smallest_even_value]
    return [smallest_even_value, min(smallest_indexes)]
