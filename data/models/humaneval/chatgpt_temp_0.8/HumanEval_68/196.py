def pluck(arr):
    even_values = [num for num in arr if num % 2 == 0]
    if not even_values:
        return []
    else:
        smallest_even = min(even_values)
        smallest_index = arr.index(smallest_even)
        return [smallest_even, smallest_index]
