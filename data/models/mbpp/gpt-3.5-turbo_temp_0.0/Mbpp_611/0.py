Here is the completed code snippet:

```python
def max_of_nth(matrix, n):
    column = [row[n] for row in matrix]
    return max(column)

assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
```

In this code, the `max_of_nth` function takes two parameters: `matrix` and `n`. It first creates a list called `column` using a list comprehension. This list comprehension iterates over each row in the matrix and selects the element at index `n` for each row. This creates a list of all the elements in the n'th column.

Finally, the function returns the maximum value from the `column` list using the `max` function.

The `assert` statement at the end of the code snippet verifies that the function returns the expected result.