Here is the completed code snippet:

```python
def remove_dirty_chars(string1, string2):
    for char in string2:
        string1 = string1.replace(char, "")
    return string1

assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
```

The `remove_dirty_chars` function takes two strings as input: `string1` and `string2`. It iterates over each character in `string2` and uses the `replace` method to remove any occurrences of that character from `string1`. Finally, it returns the modified `string1`.

The `assert` statement is used to verify that the function produces the expected output. In this case, it checks if `remove_dirty_chars("probasscurve", "pros")` returns `'bacuve'`.