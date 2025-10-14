Here is the Python function implemented in a markdown style code block:

```python
def remove_elements(list1, list2):
    return [i for i in list1 if i not in list2]

# Test the function
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
```

This function uses list comprehension to create a new list that includes only the elements from `list1` that are not in `list2`. The `assert` statement is used to test the function with the provided example.
