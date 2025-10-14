Here is the completed code snippet:

```python
def swap_List(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
```

The `swap_List` function takes a list as input and swaps the first and last elements using tuple unpacking. It then returns the modified list. The `assert` statement checks if the function produces the expected output.