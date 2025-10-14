Here is the Python function to find the first repeated character in a given string:

```python
def first_repeated_char(s):
    count = {}
    for char in s:
        if char in count:
            return char
        else:
            count[char] = 1
    return None

print(first_repeated_char("abcabc"))  # Output: a
```

This function works by creating a dictionary to keep track of the count of each character in the string. As it iterates through the string, it checks if the character is already in the dictionary. If it is, it means that character is repeated, so it returns the character. If it gets through the entire string without finding any repeated characters, it returns None.
