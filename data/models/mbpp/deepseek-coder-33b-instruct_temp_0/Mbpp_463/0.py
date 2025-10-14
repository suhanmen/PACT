Here is the Python function to find the maximum product subarray of the given array:

```python
def max_subarray_product(arr):
    max_ending_here = min_ending_here = max_so_far = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here

        max_ending_here = max(arr[i], max_ending_here * arr[i])
        min_ending_here = min(arr[i], min_ending_here * arr[i])

        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
```

This function uses the Kadane's algorithm approach to solve the problem. It keeps track of the maximum product ending at the current position and the minimum product ending at the current position. If the current number is negative, it swaps the maximum and minimum product ending at the current position. Then it updates the maximum product ending at the current position and the overall maximum product. Finally, it returns the overall maximum product.
