Here is the Python function to find the maximum value in a given heterogeneous list:

```python
def max_val(lst):
    """
    This function finds the maximum value in a given heterogeneous list.
    """
    # Filter out non-integer values
    int_lst = [i for i in lst if isinstance(i, int)]
    
    # Return the maximum value
    return max(int_lst)
```

You can use this function as follows:

```python
print(max_val(['Python', 3, 2, 4, 5, 'version']))  # Output: 5
```

This function works by first filtering out non-integer values from the list. It then finds the maximum value from the filtered list.
