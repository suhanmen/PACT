Here is the Python function that converts all possible convertible elements in a list of lists to floats:

```python
def list_to_float(lst):
    return [tuple(float(i) for i in sublist) for sublist in lst]
```

You can test this function with the provided test case:

```python
print(list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]))
```

This should output:

```python
[(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
```
