Here is the Python function to find the sum of the largest contiguous sublist in the given list:

```python
def max_sub_array_sum(arr):
    max_so_far = max_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

This function uses the Kadane's algorithm to find the maximum subarray sum. It initializes two variables, `max_so_far` and `max_ending_here`, to the first element of the array. Then it iterates over the array from the second element to the end. For each element, it updates `max_ending_here` to be the maximum of the current element and the sum of the current element and `max_ending_here`. Then it updates `max_so_far` to be the maximum of `max_so_far` and `max_ending_here`. Finally, it returns `max_so_far`, which is the sum of the maximum subarray.
