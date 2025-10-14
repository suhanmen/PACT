def pluck(arr):
    even_values = [n for n in arr if n % 2 == 0]
    if not even_values:
        return []
    smallest_even_value = min(even_values)
    smallest_even_value_index = arr.index(smallest_even_value)
    return [smallest_even_value, smallest_even_value_index]
