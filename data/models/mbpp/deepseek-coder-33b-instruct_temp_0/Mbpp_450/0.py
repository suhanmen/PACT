Here is the Python function to solve the problem:

```python
def extract_string(lst, size):
    return [s for s in lst if len(s) == size]
```

You can test the function with the following code:

```python
print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8))
```

This will output:

```python
['practice', 'solution']
```
