Here is the Python function implemented in a markdown style code block:

```python
def neg_nos(lst):
    """
    This function returns the negative numbers in a list.
    """
    return [num for num in lst if num < 0]

# Test the function
print(neg_nos([-1,4,5,-6]))  # Output: [-1,-6]
```

In this function, we use a list comprehension to iterate over the input list and select only the numbers that are less than 0. The result is a new list that contains only the negative numbers from the input list.
