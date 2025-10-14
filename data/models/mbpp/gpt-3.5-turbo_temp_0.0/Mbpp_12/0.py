Here is the completed code snippet:

```python
def sort_matrix(matrix):
    sorted_matrix = sorted(matrix, key=lambda row: sum(row))
    return sorted_matrix

assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]) == [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
```

The `sort_matrix` function takes a matrix as input and sorts it in ascending order according to the sum of its rows. The `sorted` function is used with a lambda function as the key parameter to specify that the sorting should be based on the sum of each row. The sorted matrix is then returned. The provided test case asserts that the function returns the expected result.