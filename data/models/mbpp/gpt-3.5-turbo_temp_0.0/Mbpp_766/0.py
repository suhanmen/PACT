Here is the completed code snippet:

```python
def pair_wise(lst):
    pairs = []
    for i in range(len(lst)-1):
        pairs.append((lst[i], lst[i+1]))
    return pairs

assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
```

The `pair_wise` function takes a list as input and returns a new list containing all pairs of consecutive items in the input list. It uses a for loop to iterate over the indices of the input list, and for each index `i`, it appends a tuple `(lst[i], lst[i+1])` to the `pairs` list. Finally, it returns the `pairs` list.

The `assert` statement at the end of the code snippet verifies that the `pair_wise` function produces the expected output for a given input.