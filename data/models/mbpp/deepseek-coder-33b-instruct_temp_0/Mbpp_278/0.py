Here is the Python function that solves the problem:

```python
def count_first_elements(t):
    count = 0
    for i in t:
        if isinstance(i, tuple):
            break
        count += 1
    return count
```

This function iterates over the elements in the given tuple. If it encounters a tuple element, it breaks the loop and returns the count of non-tuple elements that have been encountered so far.

You can test the function with the provided test case:

```python
print(count_first_elements((1, 5, 7, (4, 6), 10)))  # Output: 3
```

This will print `3`, which is the expected output.
