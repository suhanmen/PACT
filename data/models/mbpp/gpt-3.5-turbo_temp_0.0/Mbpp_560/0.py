Here is the completed code snippet:

```python
def union_elements(tuple1, tuple2):
    union = set(tuple1).union(set(tuple2))
    return tuple(sorted(union))

assert union_elements((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 4, 5, 6, 7, 10)
```

In this code, the `union_elements` function takes two tuples as input. It converts each tuple into a set to remove any duplicate elements. Then, it uses the `union` method to find the union of the two sets. The resulting set is then converted back into a tuple and sorted in ascending order using the `sorted` function. Finally, the sorted tuple is returned as the output.

The `assert` statement is used to verify that the function produces the expected output. In this case, it checks if the union of `(3, 4, 5, 6)` and `(5, 7, 4, 10)` is equal to `(3, 4, 5, 6, 7, 10)`. If the condition is true, the code continues execution. If the condition is false, an `AssertionError` is raised.