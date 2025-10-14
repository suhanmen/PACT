Here is the completed code snippet:

```python
def find_Rotations(string):
    n = len(string)
    for i in range(1, n):
        if string[:i] == string[i:]:
            return i
    return n

assert find_Rotations("aaaa") == 1
```

In this code, the `find_Rotations` function takes a string as input and iterates through all possible rotation positions. It checks if the substring from index 0 to `i` is equal to the substring from index `i` to the end of the string. If a match is found, it returns the number of rotations required (which is `i`). If no match is found, it returns the length of the string (`n`), indicating that no rotations are required. The `assert` statement is used to verify that the function returns the expected result for the given example.