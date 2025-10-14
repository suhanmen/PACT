def pluck(arr):
    even_values = [num for num in arr if num % 2 == 0]
    if not even_values:
        return []
    else:
        min_even = min(even_values)
        min_even_indices = [i for i, num in enumerate(arr) if num == min_even]
        return [min_even, min(min_even_indices)]
