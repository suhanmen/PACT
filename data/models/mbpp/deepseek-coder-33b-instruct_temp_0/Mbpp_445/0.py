Here is the Python function that performs index wise multiplication of tuple elements in the given two tuples:

```python
def index_multiplication(t1, t2):
    return tuple(tuple(a*b for a, b in zip(x, y)) for x, y in zip(t1, t2))
```

You can test this function with the provided test case:

```python
print(index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))))
# Output: ((6, 21), (12, 45), (2, 9), (7, 30))
```

This function works by using the `zip` function to pair up the corresponding elements from the two input tuples. Then, for each pair of tuples, it uses another `zip` function to pair up the corresponding elements from the two tuples. Finally, it multiplies the paired elements together and forms a new tuple. This process is repeated for all pairs of tuples, and the results are collected into a new tuple.
