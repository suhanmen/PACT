Here's the completed code snippet:

```python
def rotate_right(lst, n):
    n = n % len(lst)  # to handle cases where n is larger than the length of the list
    return lst[-n:] + lst[:-n]

assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
```

The `rotate_right` function takes a list `lst` and a number `n` as input. It calculates the effective rotation amount by taking the modulus of `n` with the length of the list. This ensures that the rotation amount is within the range of the list length.

The function then returns a new list that is obtained by concatenating the last `n` elements of the original list with the first `len(lst) - n` elements of the original list. This effectively rotates the list to the right by `n` positions.

The `assert` statement checks if the output of the `rotate_right` function matches the expected output `[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]`. If the assertion fails, an `AssertionError` will be raised.