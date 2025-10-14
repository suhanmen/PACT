Here is the Python function implemented in a markdown style code block:

```python
def substract_elements(tuple1, tuple2):
    return tuple(x - y for x, y in zip(tuple1, tuple2))
```

You can test this function with the provided test case:

```python
print(substract_elements((10, 4, 5), (2, 5, 18)))  # Output: (8, -1, -13)
```

This function works by using the `zip` function to pair up the elements of the two tuples with the same index, then it subtracts the second element from the first for each pair. The `tuple` function is used to convert the result back into a tuple.
