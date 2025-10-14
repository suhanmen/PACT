Here is the completed code snippet:

```python
def Diff(list1, list2):
    return [item for item in list1 if item not in list2]

assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 15, 20, 30]
```

The function `Diff` takes two lists as input and returns a new list containing the elements that are present in the first list but not in the second list. The list comprehension `[item for item in list1 if item not in list2]` is used to achieve this. The `assert` statement is used to verify that the function returns the expected result.