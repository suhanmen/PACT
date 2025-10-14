Here is the completed code snippet:

```python
def two_unique_nums(lst):
    return list(set(lst))

assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
```

In this code, the `two_unique_nums` function takes a list as input and uses the `set` function to remove duplicate elements. The resulting set is then converted back to a list using the `list` function and returned. The `assert` statement checks if the function returns the expected output for the given input.