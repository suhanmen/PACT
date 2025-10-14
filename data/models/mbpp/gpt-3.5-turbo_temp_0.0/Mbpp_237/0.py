Here is the completed code snippet:

```python
def check_occurrences(lst):
    occurrences = {}
    for item in lst:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences

assert check_occurrences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(3, 1): 1, (1, 3): 1, (2, 5): 1, (5, 2): 1, (6, 3): 1}
```

The function `check_occurrences` takes in a list of tuples `lst` as input. It initializes an empty dictionary `occurrences` to store the occurrences of each tuple. It then iterates over each item in the list. If the item is already in the `occurrences` dictionary, it increments the count by 1. Otherwise, it adds the item to the dictionary with a count of 1. Finally, it returns the `occurrences` dictionary.

The `assert` statement checks if the function returns the expected result for the given example input.