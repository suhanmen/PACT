Here is the completed code snippet:

```python
def all_unique(lst):
    return len(lst) == len(set(lst))

assert all_unique([1,2,3]) == True
```

In this code, the `all_unique` function takes a list as input and checks if the length of the list is equal to the length of the set of the list. If they are equal, it means that all the elements in the list are unique. The `set` function removes any duplicate elements from the list, so if the lengths are equal, it means there were no duplicates. The function returns `True` if all elements are unique, and `False` otherwise.

The `assert` statement is used to check if the function returns the expected result. In this case, it checks if `all_unique([1,2,3])` returns `True`. If the condition is not met, an `AssertionError` will be raised.