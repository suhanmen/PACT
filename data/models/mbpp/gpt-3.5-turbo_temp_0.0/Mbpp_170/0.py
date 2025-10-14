Here is the completed code snippet:

```python
def sum_range_list(lst, start, end):
    return sum(lst[start:end+1])

assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
```

The `sum_range_list` function takes in a list `lst` and two indices `start` and `end`. It uses the `sum` function to calculate the sum of the numbers in the list within the specified range (inclusive of both indices). The function then returns the sum.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10)` is equal to `29`. If the condition is true, the program continues execution. If the condition is false, an `AssertionError` is raised.