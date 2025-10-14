Here is the Python function implemented in a markdown style code block:

```python
def insert_element(lst, element):
    result = []
    for i in lst:
        result.append(element)
        result.append(i)
    return result
```

You can test the function with the provided test case:

```python
print(insert_element(['Red', 'Green', 'Black'] ,'c'))
```

This should output:

```python
['c', 'Red', 'c', 'Green', 'c', 'Black']
```
