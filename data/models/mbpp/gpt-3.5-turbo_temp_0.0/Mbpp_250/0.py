Here is the completed code snippet:

```python
def count_X(tup, element):
    count = 0
    for item in tup:
        if item == element:
            count += 1
    return count

assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0
```

The `count_X` function takes in a tuple `tup` and an element `element`. It initializes a count variable to 0. Then, it iterates over each item in the tuple and checks if it is equal to the element. If it is, the count is incremented by 1. Finally, the function returns the count.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4)` returns 0, which is the expected result.