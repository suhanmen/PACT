Here is the Python function to find the minimum number of rotations required to get the same string:

```python
def find_Rotations(s):
    temp = s + s
    n = len(s)

    for i in range(1, n + 1):
        substring = temp[i : n + i]
        if (s == substring):
            return i

    return n
```

This function works by creating a temporary string that is twice the length of the input string. It then checks for each possible rotation of the input string in the temporary string. If it finds a match, it returns the number of rotations. If it doesn't find a match, it returns the length of the input string, which is the number of rotations required to get the same string.

For example, if you call `find_Rotations("aaaa")`, it will return `1` because the string "aaaa" is already a rotation of itself.
