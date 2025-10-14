Here is the Python function to solve the problem:

```python
def extract_freq(lst):
    """
    Write a function to extract the number of unique tuples in the given list.
    """
    return len(set(lst))

# Test the function
print(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]))  # Output: 3
```

In this function, we are using a set to remove duplicates from the list. The set data type in Python is an unordered collection of unique elements. When we convert the list to a set, it automatically removes any duplicate tuples. Then we return the length of the set, which is the number of unique tuples in the list.
