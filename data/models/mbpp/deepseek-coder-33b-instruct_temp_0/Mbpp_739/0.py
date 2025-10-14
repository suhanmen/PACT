Here is the Python function to find the index of smallest triangular number with n digits:

```python
def find_Index(n):
    if n == 1:
        return 1
    left, right = 1, n * 10
    while left < right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 >= 10 ** (n - 1):
            right = mid
        else:
            left = mid + 1
    return left

# Test the function
print(find_Index(2))  # Output: 4
```

This function uses binary search to find the smallest index that makes the triangular number have n digits. The triangular number is calculated by the formula `n * (n + 1) / 2`. The binary search is performed on the index, and the mid-point is checked to see if it produces a triangular number with n digits. If it does, the right boundary is moved to the mid-point, otherwise, the left boundary is moved to the mid-point plus one. The binary search continues until the left boundary equals the right boundary, which is the smallest index that makes the triangular number have n digits.
