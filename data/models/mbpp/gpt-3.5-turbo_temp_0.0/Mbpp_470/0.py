Here is the completed code snippet:

```python
def add_pairwise(t):
    result = []
    for i in range(len(t) - 1):
        result.append(t[i] + t[i+1])
    return tuple(result)

assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
```

The function `add_pairwise` takes a tuple `t` as input and returns a new tuple where each element is the sum of the neighboring elements in the original tuple. The function uses a for loop to iterate over the indices of the tuple, and for each index `i`, it adds `t[i]` and `t[i+1]` and appends the result to the `result` list. Finally, the function returns the `result` list converted to a tuple.

The `assert` statement at the end of the code snippet checks if the function produces the expected output for the given example.