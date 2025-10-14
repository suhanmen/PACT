Here is the Python function implemented in a markdown style code block:

```python
def reverse_string_list(input_list):
    return [s[::-1] for s in input_list]

print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']))
```

This function uses list comprehension to reverse each string in the input list. The `[::-1]` slice is a common Python idiom for reversing a string. The function then returns the new list of reversed strings.
