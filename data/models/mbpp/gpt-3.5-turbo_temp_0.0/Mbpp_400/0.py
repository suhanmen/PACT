Here is the completed code snippet:

```python
def extract_freq(lst):
    unique_tuples = set(lst)
    return len(unique_tuples)

assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3
```

In this code, the `extract_freq` function takes a list of tuples as input. It creates a set of the tuples to remove any duplicates, and then returns the length of the set, which represents the number of unique tuples in the list. The `assert` statement is used to verify that the function returns the expected result.