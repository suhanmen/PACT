Here is the completed code snippet:

```python
from itertools import combinations_with_replacement

def combinations_colors(lst, n):
    return list(combinations_with_replacement(lst, n))

assert combinations_colors(["Red","Green","Blue"], 1) == [('Red',), ('Green',), ('Blue',)]
```

The `combinations_with_replacement` function from the `itertools` module is used to generate all combinations with repetition. The function takes in a list `lst` and a length `n` as parameters. It returns a list of tuples, where each tuple represents a combination of elements from the list. The `assert` statement is used to verify that the function returns the expected output.