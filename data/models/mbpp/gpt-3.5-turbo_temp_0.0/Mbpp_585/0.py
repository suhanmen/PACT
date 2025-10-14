Here is the completed code snippet:

```python
def expensive_items(dataset, n):
    sorted_items = sorted(dataset, key=lambda x: x['price'], reverse=True)
    return sorted_items[:n]

assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], 1) == [{'name': 'Item-2', 'price': 555.22}]
```

The `expensive_items` function takes in a dataset (a list of dictionaries) and an integer `n` as parameters. It sorts the dataset based on the 'price' key in each dictionary in descending order using the `sorted` function and a lambda function as the key argument. It then returns the first `n` items from the sorted list.

The assert statement at the end checks if the function returns the expected result for the given example.