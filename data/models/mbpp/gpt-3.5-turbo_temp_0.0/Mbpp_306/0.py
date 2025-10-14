Here is the completed code snippet:

```python
def max_sum_increasing_subseq(arr, n, i, k):
    # Initialize a list to store the maximum sum of increasing subsequence until each index
    max_sum = [0] * n

    # Initialize the maximum sum as the value of the element at index i
    max_sum[i] = arr[i]

    # Iterate from index i+1 to k
    for j in range(i+1, k+1):
        # Find the maximum sum of increasing subsequence until index j
        for l in range(i, j):
            if arr[j] > arr[l]:
                max_sum[j] = max(max_sum[j], max_sum[l] + arr[j])

    # Find the maximum sum of increasing subsequence from prefix until index k
    max_sum_k = max(max_sum)

    return max_sum_k

assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6) == 11
```

In this code, we use dynamic programming to find the maximum sum of increasing subsequence until each index. We start by initializing a list `max_sum` to store the maximum sum of increasing subsequence until each index. We then iterate from index `i+1` to `k` and for each index `j`, we find the maximum sum of increasing subsequence until index `j` by comparing the values of the elements at index `j` and all previous indices `l` between `i` and `j`. Finally, we find the maximum sum of increasing subsequence from the prefix until index `k` by taking the maximum value from the `max_sum` list.