Here is the Python function that solves the problem:

```python
def max_sum(arr):
    n = len(arr)
    inc = [0]*n
    dec = [0]*n

    # Initialize increasing sequence
    for i in range(n):
        inc[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]

    # Initialize decreasing sequence
    for i in range(n-1, -1, -1):
        dec[i] = arr[i]
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]

    # Find maximum sum of bitonic sequence
    max_sum = inc[0] + dec[0] - arr[0]
    for i in range(1, n):
        if inc[i] + dec[i] - arr[i] > max_sum:
            max_sum = inc[i] + dec[i] - arr[i]

    return max_sum
```

This function works by first initializing two arrays, `inc` and `dec`, to store the maximum sum of increasing and decreasing subsequences ending at each index of the input array, respectively. It then iterates over the input array, updating the `inc` and `dec` arrays as it goes. Finally, it iterates over the `inc` and `dec` arrays to find the maximum sum of a bitonic subsequence, which is the maximum sum of the sum of the `inc` and `dec` arrays at each index, minus the value at that index (since it is counted twice in the sum).
