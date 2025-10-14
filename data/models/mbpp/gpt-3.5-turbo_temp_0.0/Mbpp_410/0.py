Here is the completed code snippet:

```python
def min_val(lst):
    # Initialize the minimum value as the first element of the list
    min_value = lst[0]
    
    # Iterate through the list starting from the second element
    for i in range(1, len(lst)):
        # Check if the current element is smaller than the minimum value
        if lst[i] < min_value:
            # Update the minimum value
            min_value = lst[i]
    
    return min_value

# Test the function
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
```

This function finds the minimum value in a given heterogeneous list by iterating through the list and comparing each element with the current minimum value. If an element is smaller than the current minimum value, it becomes the new minimum value. Finally, the function returns the minimum value found.