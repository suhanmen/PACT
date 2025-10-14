Here's the completed code snippet:

```python
def first_repeated_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            return char
        char_count[char] = 1
    return None

assert first_repeated_char("abcabc") == "a"
```

In this code, we define a function `first_repeated_char` that takes a string as input. We initialize an empty dictionary `char_count` to keep track of the count of each character in the string.

We then iterate over each character in the string. If the character is already present in `char_count`, it means it is a repeated character, so we return it. Otherwise, we add the character to `char_count` with a count of 1.

If no repeated character is found, we return `None`.

The `assert` statement at the end checks if the function returns the expected result for the given example input.