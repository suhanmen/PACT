python
def pluck(arr):
    # check if array is empty
    if not arr:
        return []

    # find smallest even value and its index
    smallest_even = None
    smallest_even_index = None
    for i, val in enumerate(arr):
        # check if value is even and smaller than current smallest even value
        if val % 2 == 0 and (smallest_even is None or val < smallest_even):
            smallest_even = val
            smallest_even_index = i

    # if no even value found, return empty list
    if smallest_even is None:
        return []

    # return smallest even value and its index
    return [smallest_even, smallest_even_index]
