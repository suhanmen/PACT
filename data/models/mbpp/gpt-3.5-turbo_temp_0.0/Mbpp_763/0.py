Here is the completed code snippet:

```python
def find_min_diff(arr, n):
    # Sort the array in ascending order
    arr.sort()

    # Initialize the minimum difference
    min_diff = float('inf')

    # Find the minimum difference by comparing adjacent elements
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff

assert find_min_diff((1,5,3,19,18,25),6) == 1
```

This code defines a function `find_min_diff` that takes an array `arr` and its length `n` as input. It first sorts the array in ascending order using the `sort()` method. Then, it initializes the minimum difference `min_diff` to infinity.

Next, it iterates through the array and calculates the difference between each adjacent pair of elements. If the difference is smaller than the current minimum difference, it updates the `min_diff` variable.

Finally, it returns the minimum difference.

The `assert` statement at the end checks if the function returns the expected result for the given input.