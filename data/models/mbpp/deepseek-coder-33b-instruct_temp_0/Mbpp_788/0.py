Here is the Python function implemented in a markdown style code block:

```python
def new_tuple(list_input, string_input):
    """
    Write a function to create a new tuple from the given string and list.
    """
    list_input.append(string_input)
    return tuple(list_input)

# Test the function
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
```

In this function, we first append the string to the end of the list. Then, we convert the list to a tuple and return it. The assertion at the end tests the function with the given example.
