Here is the Python function implemented in a markdown style code block:

```python
def cummulative_sum(tuple_list):
    total_sum = 0
    for tup in tuple_list:
        total_sum += sum(tup)
    return total_sum

# Test the function
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
```

This function works by iterating over each tuple in the list, and for each tuple, it calculates the sum of its elements using the built-in `sum` function. This sum is then added to a running total, which is returned at the end.
