Here is the completed code snippet:

```python
def sample_nam(names):
    total_length = 0
    for name in names:
        if name[0].islower():
            continue
        total_length += len(name)
    return total_length

assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']) == 16
```

In this code, we define a function `sample_nam` that takes a list of names as input. We initialize a variable `total_length` to keep track of the sum of the lengths of the names.

We then iterate over each name in the list. If the first character of the name is lowercase, we skip that name using the `continue` statement. Otherwise, we add the length of the name to `total_length`.

Finally, we return the `total_length` after iterating through all the names.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])` is equal to `16`. If the condition is true, the code continues executing. If the condition is false, an `AssertionError` is raised.