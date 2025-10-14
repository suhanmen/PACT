Here is the completed code snippet:

```python
def sub_list(list1, list2):
    return [x - y for x, y in zip(list1, list2)]

assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
```

In this code, the `sub_list` function takes two lists as input and uses a list comprehension to subtract the corresponding elements of the two lists. The `zip` function is used to pair up the elements from the two lists, and then the subtraction operation is performed on each pair. The resulting list is returned as the output of the function.

The `assert` statement is used to verify that the function produces the expected result. In this case, it checks that `sub_list([1, 2, 3], [4, 5, 6])` returns `[-3, -3, -3]`. If the result is not as expected, an `AssertionError` will be raised.