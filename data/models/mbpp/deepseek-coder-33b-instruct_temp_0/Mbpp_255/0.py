Here is the Python function that generates all combinations (with repetition) of the elements of the list:

```python
from itertools import product

def combinations_colors(colors, n):
    return list(product(colors, repeat=n))
```

You can use this function like this:

```python
print(combinations_colors(["Red","Green","Blue"], 1))
```

This will output:

```python
[('Red',), ('Green',), ('Blue',)]
```

This function uses the `product` function from the `itertools` module to generate all combinations (with repetition) of the elements of the list. The `repeat` parameter is set to `n`, which means that each combination will have `n` elements. The `list` function is used to convert the result to a list.
