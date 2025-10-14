Here is the Python function to convert a given tuple of positive integers into a single integer:

```python
def tuple_to_int(t):
    return int(''.join(map(str, t)))

# Test the function
print(tuple_to_int((1,2,3)))  # Output: 123
```

In this function, we use the `map()` function to convert each element in the tuple to a string. Then, we use the `join()` function to concatenate all the strings into one. Finally, we use the `int()` function to convert the resulting string to an integer.
