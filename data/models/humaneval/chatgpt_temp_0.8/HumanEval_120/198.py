def maximum(arr, k):
    # Sort the array in decreasing order
    sorted_arr = sorted(arr, reverse=True)
    # Take the first k elements
    result = sorted_arr[:k]
    return result
