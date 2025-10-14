Here is the Python function to find the sum of all items in the given dictionary:

```python
def return_sum(dictionary):
    return sum(dictionary.values())

# Test the function
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
```

In this function, we use the built-in `sum()` function with `dictionary.values()` to sum up all the values in the dictionary. The `dictionary.values()` function returns a view object that displays a list of all values in a dictionary. The `sum()` function then adds up all these values.
