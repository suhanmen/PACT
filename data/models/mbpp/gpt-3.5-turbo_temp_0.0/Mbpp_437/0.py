Here is the completed code snippet:

```python
def remove_odd(string):
    return string[1::2]

assert remove_odd("python") == "yhn"
```

The `remove_odd` function takes a string as input and returns a new string with only the odd-indexed characters. The slicing notation `string[1::2]` starts from index 1 and selects every second character until the end of the string. In the example assertion, it checks if the output of `remove_odd("python")` is equal to the expected output `"yhn"`.