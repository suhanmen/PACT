Here is the completed code snippet:

```python
def check_Consecutive(lst):
    # Sort the list in ascending order
    sorted_lst = sorted(lst)
    
    # Check if the difference between consecutive elements is always 1
    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i+1] - sorted_lst[i] != 1:
            return False
    
    return True

# Test the function
assert check_Consecutive([1,2,3,4,5]) == True
```

The `check_Consecutive` function takes a list as input and checks if the elements in the list are consecutive numbers. It does this by sorting the list in ascending order and then checking if the difference between consecutive elements is always 1. If the difference is not 1 for any pair of consecutive elements, the function returns `False`. If all pairs of consecutive elements have a difference of 1, the function returns `True`.