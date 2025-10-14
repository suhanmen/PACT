Here is the Python function that solves the problem:

```python
def filter_data(students, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in students.items() if height >= min_height and weight >= min_weight}
```

This function uses a dictionary comprehension to iterate over the items in the `students` dictionary. For each item, it checks if the height and weight are both greater than or equal to the minimum height and weight. If they are, it adds the item to the new dictionary.

You can test this function with the provided test case:

```python
print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))
```

This should output:

```python
{'Cierra Vega': (6.2, 70)}
```
