Here is the completed code snippet:

```python
def merge(lst):
    result = [[], []]
    for sublist in lst:
        result[0].append(sublist[0])
        result[1].append(sublist[1])
    return result

assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
```

The `merge` function takes a list of lists as input. It initializes an empty list `result` with two sublists. Then, it iterates over each sublist in the input list and appends the first element of each sublist to the first sublist of `result` and the second element to the second sublist of `result`. Finally, it returns the `result` list. The `assert` statement checks if the output of the `merge` function matches the expected output and raises an error if they don't match.