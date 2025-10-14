Here is the Python function to find the dissimilar elements in the given two tuples:

```python
def find_dissimilar(t1, t2):
    return tuple(set(t1) ^ set(t2))
```

This function works by converting the tuples to sets, using the `^` operator to find the symmetric difference (elements that are in either of the sets, but not in both), and then converting the result back to a tuple.

You can test the function with the provided example:

```python
print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))  # Output: (3, 6, 7, 10)
```

This will print the tuple `(3, 6, 7, 10)`, which are the dissimilar elements in the given two tuples.
