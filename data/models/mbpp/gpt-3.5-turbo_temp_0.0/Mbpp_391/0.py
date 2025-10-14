Here is the completed code snippet:

```python
def convert_list_dictionary(keys, values, scores):
    result = []
    for key, value, score in zip(keys, values, scores):
        result.append({key: {value: score}})
    return result

assert convert_list_dictionary(["S001", "S002", "S003", "S004"], ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"], [85, 98, 89, 92]) == [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
```

The `convert_list_dictionary` function takes three lists as input: `keys`, `values`, and `scores`. It uses the `zip` function to iterate over the three lists simultaneously. For each iteration, it creates a nested dictionary with the current key, value, and score, and appends it to the `result` list. Finally, it returns the `result` list.

The `assert` statement is used to verify that the function produces the expected output.