Here is the Python function implemented in a markdown style code block:

```python
def sum_length_of_names(names):
    """
    This function sums the length of the names of a given list of names after removing the names that start with a lowercase letter.
    """
    return sum(len(name) for name in names if name[0].isupper())

# Test the function
print(sum_length_of_names(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))
```

This function works by iterating over each name in the list. If the first character of the name is an uppercase letter (checked using the `isupper()` method), the length of the name is added to the sum. The `sum()` function is used to add up these lengths.
