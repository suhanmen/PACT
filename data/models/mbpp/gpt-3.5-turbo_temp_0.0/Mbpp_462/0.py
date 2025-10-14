Here is the completed code snippet:

```python
def combinations_list(lst):
    result = [[]]
    for i in lst:
        result += [j + [i] for j in result]
    return result

assert combinations_list(['orange', 'red', 'green', 'blue']) == [[], ['orange'], ['red'], ['orange', 'red'], ['green'], ['orange', 'green'], ['red', 'green'], ['orange', 'red', 'green'], ['blue'], ['orange', 'blue'], ['red', 'blue'], ['orange', 'red', 'blue'], ['green', 'blue'], ['orange', 'green', 'blue'], ['red', 'green', 'blue'], ['orange', 'red', 'green', 'blue']]
```

The `combinations_list` function takes a list as input and returns a list of all possible combinations of its elements. It initializes the result list with an empty list `[]`. Then, for each element `i` in the input list, it appends a new combination to the result list by iterating over the existing combinations in the result list and adding `i` to each of them. Finally, it returns the result list.

The assert statement checks if the function produces the expected output for the given input list.