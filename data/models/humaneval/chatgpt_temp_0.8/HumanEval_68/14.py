def pluck(arr):
    even_vals = [x for x in arr if x % 2 == 0]
    if not even_vals:
        return []
    smallest = min(even_vals)
    smallest_index = arr.index(smallest)
    return [smallest, smallest_index]
