Here is the completed code snippet:

```python
def cumulative_sum(tuple_list):
    total_sum = 0
    for tup in tuple_list:
        total_sum += sum(tup)
    return total_sum

assert cumulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
```

In this code, the `cumulative_sum` function takes a list of tuples as input. It iterates over each tuple in the list and calculates the sum of all the values in each tuple using the `sum` function. The sums are then added together to get the cumulative sum. Finally, the function returns the cumulative sum.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if the cumulative sum of the given tuple list is equal to 30.