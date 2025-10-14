Here is the Python function to find the combinations of sums with tuples in the given tuple list:

```python
from itertools import combinations

def find_combinations(tuples_list):
    result = []
    for r in range(1, len(tuples_list) + 1):
        for combination in combinations(tuples_list, r):
            sums = [sum(x) for x in zip(*combination)]
            result.append(tuple(sums))
    return result
```

This function uses the `itertools.combinations` function to generate all possible combinations of tuples from the input list. For each combination, it calculates the sums of the corresponding elements from each tuple and adds the sums as a tuple to the result list.

For example, if the input is `[(2, 4), (6, 7), (5, 1), (6, 10)]`, the function will generate the following combinations:

- `[(2, 4)]`, `[(6, 7)]`, `[(5, 1)]`, `[(6, 10)]`
- `[(2, 4), (6, 7)]`, `[(2, 4), (5, 1)]`, `[(2, 4), (6, 10)]`, `[(6, 7), (5, 1)]`, `[(6, 7), (6, 10)]`, `[(5, 1), (6, 10)]`
- `[(2, 4), (6, 7), (5, 1)]`, `[(2, 4), (6, 7), (6, 10)]`, `[(2, 4), (5, 1), (6, 10)]`, `[(6, 7), (5, 1), (6, 10)]`
- `[(2, 4), (6, 7), (5, 1), (6, 10)]`

For each combination, it calculates the sums of the corresponding elements from each tuple, and adds the sums as a tuple to the result list. For example, for the combination `[(2, 4), (6, 7), (5, 1)]`, the sums are `(8, 11)`, and for the combination `[(2, 4), (6, 7), (6, 10)]`, the sums are `(7, 5)`, and so on.
