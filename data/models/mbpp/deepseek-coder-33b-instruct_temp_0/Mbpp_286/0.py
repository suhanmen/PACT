Here is the Python function that solves the problem:

```python
def max_sub_array_sum_repeated(arr, n, k):
    # Create a new array by repeating the given array k times
    new_arr = arr * k

    # Initialize:
    # max_so_far is maximum sum found so far
    # max_ending_here is maximum sum ending at current position
    max_so_far = float('-inf')
    max_ending_here = 0

    for i in range(0, n*k):
        max_ending_here = max_ending_here + new_arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
```

This function works by creating a new array by repeating the given array k times. It then uses Kadane's algorithm to find the maximum sum of a contiguous subarray in the new array.

The time complexity of this function is O(n), where n is the length of the array. This is because the function only needs to iterate through the array once.
