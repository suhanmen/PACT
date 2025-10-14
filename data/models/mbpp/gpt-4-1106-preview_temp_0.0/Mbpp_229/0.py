"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""



def re_arrange_array(arr, n):
    # Separate the array into negative and non-negative lists
    negative_elements = [x for x in arr[:n] if x < 0]
    non_negative_elements = [x for x in arr[:n] if x >= 0]
    # Combine the lists and append the remaining elements
    return negative_elements + non_negative_elements + arr[n:]

# Example usage
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
