Here is the Python function implemented in a markdown style code block:

```python
def max_sum_list(list_of_lists):
    """
    Write a function that returns the list in a list of lists whose sum of elements is the highest.
    """
    return max(list_of_lists, key=sum)

# Test the function
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
```

This function uses the built-in `max` function in Python, which returns the largest item in an iterable or the largest of two or more arguments. The `key` argument specifies a one-argument ordering function like that used for list.sort(). The `sum` function is used as the key function to calculate the sum of each list in the list of lists.
