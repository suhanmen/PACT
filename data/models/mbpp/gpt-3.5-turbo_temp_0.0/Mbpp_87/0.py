Here is the completed code snippet:

```python
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {}
    merged_dict.update(dict1)
    merged_dict.update(dict2)
    merged_dict.update(dict3)
    return merged_dict

assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }) == {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
```

The `merge_dictionaries_three` function takes three dictionaries as input (`dict1`, `dict2`, `dict3`) and creates an empty dictionary `merged_dict`. It then uses the `update` method to merge the three dictionaries into `merged_dict`. Finally, it returns the merged dictionary.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if the merged dictionary is equal to `{'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}`. If the assertion fails, an error will be raised.