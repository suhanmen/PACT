Here is the Python function to solve the problem:

```python
def magic_square_test(matrix):
    # Get the size of the matrix
    size = len(matrix)

    # Calculate the sum of the first row
    magic_sum = sum(matrix[0])

    # Check the sum of each row
    for row in matrix:
        if sum(row) != magic_sum:
            return False

    # Check the sum of each column
    for col in range(size):
        if sum(row[col] for row in matrix) != magic_sum:
            return False

    # Check the sum of the diagonals
    if sum(matrix[i][i] for i in range(size)) != magic_sum or \
       sum(matrix[i][size-i-1] for i in range(size)) != magic_sum:
        return False

    return True
```

You can test the function with the provided example:

```python
print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))  # Output: True
```

This function works by first calculating the sum of the first row. It then checks each row, each column, and both diagonals to see if they all have the same sum. If they do, the function returns `True`, indicating that the matrix is a magic square. If any of these sums do not match the first row's sum, the function returns `False`.
