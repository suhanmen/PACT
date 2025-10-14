Here's the completed code snippet:

```python
def odd_length_sum(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        for j in range(i, n, 2):
            for k in range(i, j+1):
                result += arr[k]
    return result

assert odd_length_sum([1,2,4]) == 14
```

The `odd_length_sum` function takes an array `arr` as input and calculates the sum of all odd length subarrays. It uses three nested loops to iterate through all possible subarrays and adds up the elements within each subarray to the `result` variable. Finally, it returns the `result` as the output.

The `assert` statement at the end of the code snippet is used to verify that the function produces the expected output for the given example.