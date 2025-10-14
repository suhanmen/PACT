Here is the completed code snippet:

```python
def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]

assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4) == [4, 3, 2, 1, 5, 6]
```

In this code, the `reverse_Array_Upto_K` function takes an array `arr` and a position `k` as input. It slices the array from index 0 to `k` (exclusive) and reverses it using the `[::-1]` slicing syntax. Then, it concatenates the reversed slice with the remaining elements of the array from index `k` onwards. The resulting reversed array is returned. The `assert` statement checks if the function returns the expected output for the given example.