Here is the Python function to solve the problem:

```python
def sort_matrix(matrix):
    return sorted(matrix, key=sum)
```

This function uses the built-in `sorted` function in Python, which sorts an iterable and returns a new sorted list of the elements in the iterable. The `key` parameter is a function that serves as a key or a basis of sort comparison. In this case, we use the built-in `sum` function as the key, which calculates the sum of the elements in each row of the matrix.

You can test this function with the provided test case:

```python
print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))
```

This should output:

```python
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
```

This means the function works as expected.
