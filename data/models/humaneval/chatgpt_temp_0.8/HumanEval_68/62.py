def pluck(arr):
    even_values = [num for num in arr if num % 2 == 0]
    if not even_values:
        return []
    smallest_value = min(even_values)
    smallest_index = arr.index(smallest_value)
    return [smallest_value, smallest_index]
