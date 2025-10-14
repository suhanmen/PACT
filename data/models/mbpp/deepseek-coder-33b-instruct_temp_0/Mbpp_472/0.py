Here is the Python function to check whether the given list contains consecutive numbers or not:

```python
def check_Consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst)+1))

print(check_Consecutive([1,2,3,4,5])) # True
```

This function works by first sorting the list and then comparing it to a list of consecutive numbers from the minimum to the maximum value in the original list. If the sorted list is equal to this list, then the original list contains consecutive numbers.
