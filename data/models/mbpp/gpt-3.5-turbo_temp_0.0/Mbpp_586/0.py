Here is the completed code snippet:

```python
def split_Arr(arr, n):
    return arr[n:] + arr[:n]

assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
```

The `split_Arr` function takes in a list `arr` and an integer `n`. It splits the list at the `n`th element using slicing and then concatenates the second part of the list with the first part using the `+` operator. The resulting list is returned.

The `assert` statement is used to verify that the function produces the expected output. In this case, it checks if `split_Arr([12,10,5,6,52,36],2)` is equal to `[5,6,52,36,12,10]`. If the condition is true, the program continues execution. If the condition is false, an `AssertionError` is raised.