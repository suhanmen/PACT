Here is the Python function to convert the given tuple to a key-value dictionary using adjacent elements:

```python
def tuple_to_dict(tup):
    return {tup[i]: tup[i + 1] for i in range(0, len(tup), 2)}
```

You can test this function with the given example:

```python
print(tuple_to_dict((1, 5, 7, 10, 13, 5)))  # Output: {1: 5, 7: 10, 13: 5}
```

This function works by iterating over the tuple with a step of 2 (`range(0, len(tup), 2)`), and for each iteration, it creates a new key-value pair in the dictionary. The key is the current element (`tup[i]`), and the value is the next element (`tup[i + 1]`).
