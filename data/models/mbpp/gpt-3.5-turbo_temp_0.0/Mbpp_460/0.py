Here is the completed code snippet:

```python
def Extract(lst):
    return [sublist[0] for sublist in lst]

assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
```

The function `Extract` takes a list of sublists as input. It uses a list comprehension to iterate over each sublist and extract the first element of each sublist. The extracted elements are then returned as a new list. The `assert` statement checks if the output of the function matches the expected output `[1, 3, 6]`.