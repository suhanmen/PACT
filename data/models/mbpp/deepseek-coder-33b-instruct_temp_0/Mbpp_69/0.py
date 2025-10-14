Here is the Python function to check whether a list contains the given sublist or not:

```python
def is_sublist(main_list, sublist):
    sub_len = len(sublist)
    for i in range(len(main_list)):
        if main_list[i:i+sub_len] == sublist:
            return True
    return False
```

You can test the function with the following code:

```python
print(is_sublist([2,4,3,5,7],[3,7])) # False
```

This function works by iterating over the main list and checking if the sublist is equal to the slice of the main list starting at the current index and of length equal to the sublist. If it finds a match, it returns True. If it doesn't find a match after checking all possible slices, it returns False.
