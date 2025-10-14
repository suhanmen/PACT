Here is the Python function implemented in a markdown style code block:

```python
def replace_specialchar(s):
    for char in [' ', ',', '.']:
        s = s.replace(char, ':')
    return s
```

You can test the function with the following code:

```python
print(replace_specialchar('Python language, Programming language.'))
```

This should output:

```python
'Python:language::Programming:language:'
```
