def pluck(arr):
    even_values = [n for n in arr if n % 2 == 0]
    if len(even_values) == 0:
        return []
    else:
        smallest_value = min(even_values)
        smallest_index = arr.index(smallest_value)
        return [smallest_value, smallest_index]
