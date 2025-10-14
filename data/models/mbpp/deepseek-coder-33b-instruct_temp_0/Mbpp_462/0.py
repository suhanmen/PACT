Here is the Python function to find all possible combinations of the elements of a given list:

```python
from itertools import combinations

def combinations_list(lst):
    result = []
    for i in range(len(lst) + 1):
        result += list(combinations(lst, i))
    return result
```

This function uses the `combinations` function from the `itertools` module to generate all possible combinations of the elements in the list. The `range(len(lst) + 1)` generates all possible lengths of combinations (from 0 to the length of the list), and for each length, it generates all combinations of that length. The results are then combined into a single list.

You can test this function with the provided test case:

```python
print(combinations_list(['orange', 'red', 'green', 'blue']))
```

This should output the same list as in the assertion in your question.
