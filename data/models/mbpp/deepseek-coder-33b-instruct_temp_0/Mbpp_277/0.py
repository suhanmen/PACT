Here is the Python function implemented in a markdown style code block:

```python
def dict_filter(dictionary, n):
    return {k: v for k, v in dictionary.items() if v >= n}
```

You can test this function with the provided example:

```python
print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170))
```

This should output:

```python
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
```
