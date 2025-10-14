Here is the completed code snippet:

```python
def max_sum(arr):
    n = len(arr)
    inc = [0] * n
    dec = [0] * n

    inc[0] = arr[0]
    dec[n-1] = arr[n-1]

    for i in range(1, n):
        inc[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]

    for i in range(n-2, -1, -1):
        dec[i] = arr[i]
        for j in range(i+1, n):
            if arr[i] > arr[j] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]

    max_sum = inc[0] + dec[0]
    for i in range(1, n):
        max_sum = max(max_sum, inc[i] + dec[i])

    return max_sum

assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
```

The function `max_sum` takes an array `arr` as input and finds the maximum sum of a bitonic subsequence for the given array. It uses dynamic programming to calculate the maximum increasing sum (`inc`) and maximum decreasing sum (`dec`) for each element in the array. Finally, it calculates the maximum sum by adding the corresponding increasing and decreasing sums for each element and returns the result. The provided test case is also included to verify the correctness of the function.