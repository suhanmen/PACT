Here's the completed code snippet:

```python
from itertools import combinations

def find_combinations(tuple_list):
    result = []
    for tuple_pair in combinations(tuple_list, 2):
        sum_tuple = tuple(map(sum, zip(*tuple_pair)))
        result.append(sum_tuple)
    return result

assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
```

The `find_combinations` function takes a list of tuples as input. It uses the `combinations` function from the `itertools` module to generate all possible pairs of tuples from the input list. For each pair, it calculates the sum of corresponding elements using `zip` and `map` functions, and creates a new tuple with the sums. This tuple is then appended to the `result` list. Finally, the function returns the `result` list.

The `assert` statement at the end verifies that the function produces the expected output for the given example.