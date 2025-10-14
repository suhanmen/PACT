Here is the Python function to remove first and last occurrence of a given character from the string:

```python
def remove_Occ(s, c):
    first = s.find(c)
    last = s.rfind(c)
    if first != -1 and last != -1:
        s = s[:first] + s[first+1:last] + s[last+1:]
    return s
```

You can test the function with the following code:

```python
print(remove_Occ("hello","l"))  # Output: "heo"
```

This function works by first finding the first and last occurrence of the character in the string. If both occurrences are found, it removes the first and last occurrence by concatenating the parts of the string before and after these occurrences. If either the first or the last occurrence is not found, it simply returns the original string.
