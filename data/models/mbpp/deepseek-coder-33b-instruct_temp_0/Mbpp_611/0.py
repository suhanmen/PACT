Here is the Python function implemented in a markdown style code block:

```python
def max_of_nth(matrix, n):
    """
    Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    """
    return max(row[n-1] for row in matrix)
```

This function works by using a generator expression to iterate over each row in the matrix and select the n-th element (Python uses 0-based indexing, so we subtract 1 from n). The built-in max function then returns the maximum value of these elements.
