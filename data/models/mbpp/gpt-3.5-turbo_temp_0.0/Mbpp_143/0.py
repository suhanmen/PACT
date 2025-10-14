Here is the completed code snippet:

```python
def find_lists(tup):
    count = 0
    for item in tup:
        if isinstance(item, list):
            count += 1
    return count

assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
```

The `find_lists` function takes a tuple as input and iterates over each item in the tuple. If an item is a list, it increments the count variable. Finally, it returns the count of lists found in the tuple.

The assert statement checks if the function returns the expected result. In this case, it checks if the function correctly identifies that there are 2 lists in the given tuple.