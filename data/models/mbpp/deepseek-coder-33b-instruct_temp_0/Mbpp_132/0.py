Here is the Python function to convert a tuple to a string:

```python
def tup_string(tup):
    return ''.join(tup)

# Test the function
print(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))  # Output: exercises
```

In this function, we use the `join()` method to concatenate all the elements of the tuple into a single string. The `join()` method is a string method and returns a string in which the elements of sequence have been joined by str separator.
