def pluck(arr):
    if not arr:
        # if array is empty, return an empty list
        return []

    smallest_even = float('inf')
    smallest_even_index = None

    for i, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_even:
            smallest_even = num
            smallest_even_index = i

    if smallest_even_index is None:
        # if no even values are found, return an empty list
        return []

    return [smallest_even, smallest_even_index]
