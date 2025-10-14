Here is the Python function that solves the problem:

```python
def freq_count(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict
```

This function works by iterating over each item in the input list. If the item is already in the dictionary, it increments the count for that item. If the item is not in the dictionary, it adds it with a count of 1. The function finally returns the dictionary.
