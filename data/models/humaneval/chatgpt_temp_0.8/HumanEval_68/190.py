python
def pluck(arr):
    even_values = [x for x in arr if x % 2 == 0]
    if not even_values:
        return []
    smallest_even_value = min(even_values)
    smallest_even_index = arr.index(smallest_even_value)
    return [smallest_even_value, smallest_even_index]
