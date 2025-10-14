def maximum(arr, k):
    # Sort the array in descending order
    arr_sorted = sorted(arr, reverse=True)
    # Return the first k elements
    return arr_sorted[:k]
