Here is the completed code snippet:

```python
def issort_list(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

assert issort_list([1,2,4,6,8,10,12,14,16,17]) == True
```

The `issort_list` function takes a list as input and checks whether it is sorted or not. It does this by iterating through the list and comparing each element with the next element. If any element is greater than the next element, it means the list is not sorted and the function returns `False`. If the loop completes without finding any out-of-order elements, it means the list is sorted and the function returns `True`.

The `assert` statement at the end of the code snippet is used to verify that the function behaves as expected. It checks whether `issort_list([1,2,4,6,8,10,12,14,16,17])` returns `True`. If the condition is `False`, an `AssertionError` is raised.