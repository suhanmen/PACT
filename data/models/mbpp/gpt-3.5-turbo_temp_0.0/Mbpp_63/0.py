Here is the completed code snippet:

```python
def max_difference(tuple_list):
    max_diff = 0
    for tuple_pair in tuple_list:
        diff = abs(tuple_pair[0] - tuple_pair[1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
```

In this code, the `max_difference` function takes a list of tuples as input. It initializes a variable `max_diff` to 0, which will store the maximum difference between pairs. 

The function then iterates over each tuple pair in the input list. For each pair, it calculates the absolute difference between the first and second elements using `abs(tuple_pair[0] - tuple_pair[1])`. If this difference is greater than the current `max_diff`, it updates `max_diff` to the new value.

Finally, the function returns the maximum difference.

The `assert` statement at the end of the code snippet verifies that the function returns the expected result for the given example input.