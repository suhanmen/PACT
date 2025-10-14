Here is the Python function to find the size in bytes of the given tuple:

```python
import sys

def tuple_size(t):
    return sys.getsizeof(t)

# Test the function
assert tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
```

This function uses the `sys.getsizeof()` function to get the size of the tuple in bytes. The `assert` statement is used to test the function. If the function is correct, it will not raise an `AssertionError`.
