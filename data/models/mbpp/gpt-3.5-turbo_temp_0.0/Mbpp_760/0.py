Here is the completed code snippet:

```python
def unique_Element(numbers):
    distinct_elements = set(numbers)
    return len(distinct_elements) == 1

assert unique_Element([1,1,1]) == True
```

In this code, the `unique_Element` function takes a list of numbers as input. It creates a set of the numbers to remove any duplicates. Then, it checks if the length of the set is equal to 1, indicating that there is only one distinct element in the list. The function returns `True` if this condition is met, and `False` otherwise.

The `assert` statement is used to verify that the function behaves as expected. In this case, it checks if `unique_Element([1,1,1])` returns `True`. If the condition is not met, an `AssertionError` will be raised.