Here is the Python function implemented in a markdown style code block:

```python
def count_char_position(s):
    count = 0
    s = s.lower()
    for i in range(len(s)):
        if i == ord(s[i]) - ord('a'):
            count += 1
    return count
```

This function works by iterating over each character in the string. It converts the character to lowercase and checks if its position in the string (`i`) is equal to its position in the English alphabet (`ord(s[i]) - ord('a')`). If it is, it increments the count. Finally, it returns the count.

You can test this function with the provided test case:

```python
print(count_char_position("xbcefg"))  # Output: 2
```

This will output `2`, as the characters `b` and `f` are at the same position in the string as in the English alphabet.
