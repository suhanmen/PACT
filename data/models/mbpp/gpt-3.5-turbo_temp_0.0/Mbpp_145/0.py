Here is the completed code snippet:

```python
def max_Abs_Diff(arr):
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

assert max_Abs_Diff((2,1,5,3)) == 4
```

This function iterates through all possible pairs of elements in the given array and calculates the absolute difference between them. It keeps track of the maximum difference found so far and returns it at the end. The assert statement checks if the function returns the expected result for the given example.