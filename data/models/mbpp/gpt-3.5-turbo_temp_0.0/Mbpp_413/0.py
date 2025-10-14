Here is the completed code snippet:

```python
def extract_nth_element(lst, n):
    return [t[n] for t in lst]

assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0) == ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
```

The `extract_nth_element` function takes a list of tuples `lst` and an index `n` as input. It uses a list comprehension to extract the `n`th element from each tuple in the list and returns the resulting list. The assertion statement checks if the function returns the expected output.