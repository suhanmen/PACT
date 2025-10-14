Here is the completed code snippet:

```python
def remove_elements(list1, list2):
    return [x for x in list1 if x not in list2]

assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
```

The `remove_elements` function takes two lists as input: `list1` and `list2`. It uses a list comprehension to create a new list that contains only the elements from `list1` that are not present in `list2`. The resulting list is then returned.

The `assert` statement is used to verify that the function produces the expected output. In this case, it checks if the result of calling `remove_elements` with the given input lists is equal to `[1, 3, 5, 7, 9, 10]`. If the assertion fails, an `AssertionError` will be raised.