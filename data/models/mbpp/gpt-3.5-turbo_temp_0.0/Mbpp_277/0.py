Here is the completed code snippet:

```python
def dict_filter(dictionary, n):
    filtered_dict = {}
    for key, value in dictionary.items():
        if value >= n:
            filtered_dict[key] = value
    return filtered_dict

assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170) == {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
```

The `dict_filter` function takes in a dictionary and an integer `n`. It iterates over each key-value pair in the dictionary and checks if the value is greater than or equal to `n`. If it is, the key-value pair is added to a new dictionary called `filtered_dict`. Finally, the `filtered_dict` is returned.

The `assert` statement is used to verify that the function produces the expected output. In this case, it checks if the filtered dictionary matches the expected output dictionary.