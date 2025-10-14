Here is the completed code snippet:

```python
def larg_nnum(lst, n):
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[:n]

assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2)) == set([100, 90])
```

The `larg_nnum` function takes in a list `lst` and an integer `n`. It first sorts the list in descending order using the `sorted` function with the `reverse=True` parameter. Then, it returns a sublist containing the first `n` elements of the sorted list.

The `assert` statement checks if the output of the function matches the expected output, which is a set containing the two largest numbers from the given list.