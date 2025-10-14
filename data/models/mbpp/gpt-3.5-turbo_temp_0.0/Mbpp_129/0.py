Here is the completed code snippet:

```python
def magic_square_test(matrix):
    n = len(matrix)
    # Calculate the sum of the first row
    target_sum = sum(matrix[0])
    
    # Check if the sum of each row is equal to the target sum
    for row in matrix:
        if sum(row) != target_sum:
            return False
    
    # Check if the sum of each column is equal to the target sum
    for col in range(n):
        col_sum = sum(matrix[row][col] for row in range(n))
        if col_sum != target_sum:
            return False
    
    # Check if the sum of the main diagonal is equal to the target sum
    main_diag_sum = sum(matrix[i][i] for i in range(n))
    if main_diag_sum != target_sum:
        return False
    
    # Check if the sum of the secondary diagonal is equal to the target sum
    sec_diag_sum = sum(matrix[i][n-i-1] for i in range(n))
    if sec_diag_sum != target_sum:
        return False
    
    return True

assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True
```

The `magic_square_test` function takes a matrix as input and checks if it is a magic square. It does this by calculating the target sum (the sum of the first row) and then checking if the sum of each row, each column, and each diagonal is equal to the target sum. If any of these sums are not equal to the target sum, the function returns False. If all sums are equal to the target sum, the function returns True.