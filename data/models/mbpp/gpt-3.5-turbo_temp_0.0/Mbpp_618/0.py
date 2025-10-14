Here is the completed code snippet:

```python
def div_list(list1, list2):
    return [float(x) / y for x, y in zip(list1, list2)]

assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
```

In this code, the `div_list` function takes two lists as input (`list1` and `list2`). It uses a list comprehension to iterate over the corresponding elements of both lists and divide them. The result is a new list with the division results. The `float` function is used to ensure that the division result is a float. Finally, an assertion is made to check if the function returns the expected result.