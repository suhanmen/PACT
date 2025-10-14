Here is the completed code snippet:

```python
from itertools import combinations

def sum_Of_Subarray_Prod(lst):
    result = 0
    for i in range(1, len(lst) + 1):
        for sublst in combinations(lst, i):
            product = 1
            for num in sublst:
                product *= num
            result += product
    return result

assert sum_Of_Subarray_Prod([1,2,3]) == 20
```

This code defines a function `sum_Of_Subarray_Prod` that takes a list `lst` as input. It uses the `combinations` function from the `itertools` module to generate all possible sublists of `lst` of different lengths. For each sublist, it calculates the product of all its elements and adds it to the `result` variable. Finally, it returns the `result` variable.

The `assert` statement at the end of the code snippet checks if the function returns the expected result for the given input `[1,2,3]`.