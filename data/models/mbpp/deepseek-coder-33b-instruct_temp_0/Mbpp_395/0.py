Here is the Python function to find the first non-repeated character in a given string:

```python
def first_non_repeating_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None
```

You can use this function like this:

```python
print(first_non_repeating_character("abcabc"))  # Output: None
```

This function works by first counting the number of occurrences of each character in the string. Then it iterates over the string again and returns the first character that has a count of 1 (i.e., it's the first non-repeated character). If no such character is found, it returns `None`.
