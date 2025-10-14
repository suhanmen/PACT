Here is the Python function to convert more than one list to nested dictionary:

```python
def convert_list_dictionary(keys, names, marks):
    return [{k: {n: m}} for k, n, m in zip(keys, names, marks)]
```

You can test this function with the provided test case:

```python
print(convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92]))
```

This should output:

```python
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
```

This function works by using a list comprehension to create a new list of dictionaries. The `zip` function is used to iterate over the three input lists simultaneously. For each iteration, a new dictionary is created with the current elements from the three lists.
