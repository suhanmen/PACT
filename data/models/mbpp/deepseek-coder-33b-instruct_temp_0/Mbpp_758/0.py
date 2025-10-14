Here is the Python function implemented in a markdown style code block:

```python
def unique_sublists(lst):
    result = {}
    for sublist in lst:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in result:
            result[sublist_tuple] += 1
        else:
            result[sublist_tuple] = 1
    return result
```

This function works by iterating over each sublist in the input list. It converts each sublist to a tuple and checks if this tuple is already a key in the result dictionary. If it is, it increments the value associated with that key by 1. If it isn't, it adds the tuple to the dictionary with a value of 1. The function finally returns the result dictionary.
