Here is the completed code snippet:

```python
def big_diff(lst):
    return max(lst) - min(lst)

assert big_diff([1,2,3,4]) == 3
```

The `big_diff` function takes a list as input and returns the difference between the largest and smallest values in the list. The `max` function is used to find the largest value in the list, and the `min` function is used to find the smallest value. The difference between these two values is then returned. The `assert` statement is used to verify that the function returns the expected result for the given example.