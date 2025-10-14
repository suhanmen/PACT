Here is the completed code snippet:

```python
def extract_string(string_list, size):
    result = []
    for string in string_list:
        if len(string) == size:
            result.append(string)
    return result

assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
```

The `extract_string` function takes in a list of strings (`string_list`) and a specified size (`size`). It iterates through each string in the list and checks if its length is equal to the specified size. If it is, the string is added to the `result` list. Finally, the function returns the `result` list.

The `assert` statement is used to verify that the function produces the expected output. In this case, it checks if calling `extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8)` returns `['practice', 'solution']`. If the assertion fails, an `AssertionError` will be raised.