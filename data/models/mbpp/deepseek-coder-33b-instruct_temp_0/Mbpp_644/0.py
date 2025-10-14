Here is the Python function to reverse an array upto a given position:

```python
def reverse_Array_Upto_K(arr, k):
    arr[:k] = arr[k-1::-1]
    return arr
```

You can test the function with the following code:

```python
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4))  # Output: [4, 3, 2, 1, 5, 6]
```

This function works by slicing the array up to the given position (k), reversing it, and then replacing the original slice with the reversed slice.
