Here is the completed code snippet:

```python
def is_Sub_Array(arr, sub_arr):
    # Check if the sublist is empty
    if len(sub_arr) == 0:
        return True
    
    # Check if the sublist is longer than the main list
    if len(sub_arr) > len(arr):
        return False
    
    # Iterate through the main list
    for i in range(len(arr)):
        # Check if the current element in the main list matches the first element in the sublist
        if arr[i] == sub_arr[0]:
            # Check if the remaining elements in the main list match the elements in the sublist
            if arr[i:i+len(sub_arr)] == sub_arr:
                return True
    
    return False

# Test the function
assert is_Sub_Array([1,4,3,5],[1,2]) == False
```

This function takes two lists as input: `arr` (the main list) and `sub_arr` (the sublist). It first checks if the sublist is empty, in which case it returns `True` since an empty list is always a sublist of any list. Then it checks if the sublist is longer than the main list, in which case it returns `False` since the sublist cannot be a sublist of a shorter list. 

If neither of these conditions are met, the function iterates through the main list and checks if the current element matches the first element in the sublist. If it does, it checks if the remaining elements in the main list match the elements in the sublist by slicing the main list from the current index to the current index plus the length of the sublist. If the sliced portion of the main list matches the sublist, the function returns `True`. If no match is found, the function returns `False`.