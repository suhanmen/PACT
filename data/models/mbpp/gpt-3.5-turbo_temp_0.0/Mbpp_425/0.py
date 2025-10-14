Here is the completed code snippet:

```python
def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if element in sublist:
            count += 1
    return count

assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1) == 3
```

The `count_element_in_list` function takes in a list `lst` and an element `element` as parameters. It initializes a variable `count` to 0. Then, it iterates over each sublist in `lst` and checks if `element` is present in the sublist. If it is, it increments the `count` variable by 1. Finally, it returns the `count` value.

The `assert` statement at the end of the code snippet verifies that the function produces the expected result. In this case, it checks if the function correctly counts the number of sublists containing the element 1 in the given list.