Here is the Python function to find the minimum value in a given heterogeneous list:

```python
def min_val(lst):
    """
    This function finds the minimum value in a given heterogeneous list.
    """
    # Filter out non-integer values
    int_lst = [i for i in lst if isinstance(i, int)]
    
    # Return the minimum value
    return min(int_lst)
```

You can use this function as follows:

```python
print(min_val(['Python', 3, 2, 4, 5, 'version']))  # Output: 2
```

This function works by first filtering out non-integer values from the list. It then finds the minimum value from the filtered list.
