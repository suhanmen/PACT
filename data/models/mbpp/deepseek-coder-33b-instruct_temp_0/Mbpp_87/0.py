Here is the Python function to merge three dictionaries into a single dictionary:

```python
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict
```

You can use this function as follows:

```python
dict1 = { "R": "Red", "B": "Black", "P": "Pink" }
dict2 = { "G": "Green", "W": "White" }
dict3 = { "O": "Orange", "W": "White", "B": "Black" }

merged_dict = merge_dictionaries_three(dict1, dict2, dict3)
print(merged_dict)
```

This will output:

```python
{'R': 'Red', 'B': 'Black', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
```

Please note that if there are any duplicate keys in the dictionaries, the value from the last dictionary will be used. In this case, the value for 'W' and 'B' in the final dictionary will be 'White' and 'Black' respectively, as they are the values from the last dictionary.
