Here is the completed code snippet:

```python
def is_samepatterns(colors, patterns):
    pattern_dict = {}
    for i in range(len(colors)):
        if colors[i] not in pattern_dict:
            pattern_dict[colors[i]] = patterns[i]
        elif pattern_dict[colors[i]] != patterns[i]:
            return False
    return True

assert is_samepatterns(["red","green","green"], ["a", "b", "b"]) == True
```

The `is_samepatterns` function takes two arrays as input: `colors` and `patterns`. It checks whether the elements in the `colors` array follow the corresponding elements in the `patterns` array. The function uses a dictionary, `pattern_dict`, to keep track of the patterns associated with each color. If a color is encountered for the first time, its pattern is added to the dictionary. If a color is encountered again, its pattern is checked against the pattern in the dictionary. If they are not the same, the function returns `False`. If all the patterns match, the function returns `True`.

The `assert` statement at the end of the code snippet checks whether the function returns the expected result for the given example input.