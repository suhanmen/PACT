Here is the completed code snippet:

```
def kth_element(arr, k):
    arr.sort()
    return arr[k-1]

assert kth_element([12,3,5,7,19], 2) == 3
```

In this code, the `kth_element` function takes an array `arr` and an integer `k` as input. It first sorts the array in ascending order using the `sort()` method. Then, it returns the element at index `k-1` since the array is 0-based indexed. The `assert` statement is used to verify that the function returns the expected result.