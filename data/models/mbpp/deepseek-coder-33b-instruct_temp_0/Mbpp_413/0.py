Here is the Python function to extract the nth element from a given list of tuples:

```python
def extract_nth_element(lst, n):
    return [x[n] for x in lst]
```

You can test this function with the provided test case:

```python
print(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0))
```

This should output:

```python
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
```
