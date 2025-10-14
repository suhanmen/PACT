def pluck(arr):
    even_values = [num for num in arr if num % 2 == 0]
    if not even_values:
        return []
    else:
        smallest_even_value = min(even_values)
        indices_of_smallest_even_value = [i for i, num in enumerate(arr) if num == smallest_even_value]
        return [smallest_even_value, indices_of_smallest_even_value[0]]
