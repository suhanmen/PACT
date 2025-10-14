Here is the Python function implemented in a markdown style code block:

```python
def frequency(lst, num):
    """
    Write a function to count the number of occurrences of a number in a given list.
    """
    return lst.count(num)

# Test the function
assert frequency([1,2,3], 4) == 0
```

In this function, we use the built-in `count` method of Python lists to count the number of occurrences of a number in the list. The `count` method returns the number of times the specified element appears in the list. If the element is not found, it returns 0.
