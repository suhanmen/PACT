Here is the Python function implemented in a markdown style code block:

```python
def sequential_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return (True, i)
    return (False, -1)

# Test the function
print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))  # Expected output: (True, 3)
```

This function uses a for loop to iterate over the array. If the current element is equal to the target element, it returns a tuple containing `True` and the current index. If the loop finishes without finding the element, it returns a tuple containing `False` and `-1`.
