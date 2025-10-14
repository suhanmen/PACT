Here is the Python function to check whether the given array is monotonic or not:

```python
def is_Monotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

print(is_Monotonic([6, 5, 4, 4]))  # True
```

This function works by checking if all elements in the array are either less than or equal to the next element (for a non-decreasing array) or greater than or equal to the next element (for a non-increasing array). If either of these conditions is true, the function returns `True`, indicating that the array is monotonic. Otherwise, it returns `False`.
