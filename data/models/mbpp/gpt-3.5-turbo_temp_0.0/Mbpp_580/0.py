Here is the completed code snippet:

```python
def extract_even(t):
    if isinstance(t, tuple):
        return tuple(extract_even(x) for x in t if x % 2 == 0)
    else:
        return t
```

This function recursively checks each element in the nested tuple. If an element is a tuple, it calls the `extract_even` function on that tuple. If an element is an even number, it is included in the result. If an element is an odd number, it is excluded from the result. The function returns the modified tuple with only the even elements.