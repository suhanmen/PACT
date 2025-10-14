Here is the Python function to solve the problem:

```python
def maximize_elements(t1, t2):
    return tuple((max(a, b) for a, b in zip(t1[i], t2[i])) for i in range(len(t1)))
```

This function uses a generator expression to iterate over the tuples in `t1` and `t2` simultaneously. For each pair of tuples, it uses the `zip` function to iterate over the corresponding elements in the tuples. For each pair of elements, it uses the `max` function to find the maximum value. The result is a new tuple of the maximum values.

You can test the function with the provided example:

```python
print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))))
```

This should output:

```python
((6, 7), (4, 9), (2, 9), (7, 10))
```
