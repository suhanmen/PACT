Here is the completed code snippet:

```python
def sum_list(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

assert sum_list([10,20,30],[15,25,35])==[25,45,65]
```

The `sum_list` function takes two lists as input and uses a list comprehension to iterate over corresponding elements of the two lists and calculate their sum. The `zip` function is used to pair up the elements from the two lists. The resulting list of sums is then returned. The `assert` statement is used to verify that the function produces the expected output.