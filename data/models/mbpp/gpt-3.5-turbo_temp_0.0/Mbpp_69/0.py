Here is the completed code snippet:

```python
def is_sublist(lst, sublist):
    if len(sublist) > len(lst):
        return False
    for i in range(len(lst) - len(sublist) + 1):
        if lst[i:i+len(sublist)] == sublist:
            return True
    return False

assert is_sublist([2,4,3,5,7],[3,7]) == False
```

The `is_sublist` function takes two arguments: `lst` (the main list) and `sublist` (the sublist to check for). It first checks if the length of the sublist is greater than the length of the main list, in which case it returns `False` immediately.

Then, it iterates over the main list using a sliding window approach. For each window of length equal to the sublist, it checks if the window is equal to the sublist. If a match is found, it returns `True`. If no match is found after iterating through all possible windows, it returns `False`.

The `assert` statement at the end checks if the function returns the expected result for the given example.