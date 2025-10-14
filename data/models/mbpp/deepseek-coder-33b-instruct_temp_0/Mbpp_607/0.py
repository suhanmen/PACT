Here is the Python function that matches the given problem statement:

```python
import re

def find_literals(string, pattern):
    match = re.search(pattern, string)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return None
```

This function uses the `re.search` function to find the first occurrence of the pattern in the string. If a match is found, it returns a tuple containing the matched substring, the start index, and the end index. If no match is found, it returns `None`.

You can test this function with the provided test case:

```python
print(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'))
```

This should output:

```python
('fox', 16, 19)
```
