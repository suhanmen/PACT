Here is the Python function to rotate a given list by specified number of items to the right direction:

```python
def rotate_right(lst, n):
    return lst[-n:] + lst[:-n]
```

You can test the function with the provided example:

```python
print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))
```

This should output:

```python
[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
```
