Here is the Python function to find the n most expensive items in a given dataset:

```python
def expensive_items(items, n):
    # Sort the items by price in descending order
    items.sort(key=lambda x: x['price'], reverse=True)
    # Return the first n items
    return items[:n]
```

You can test the function with the provided test case:

```python
print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))
```

This should output:

```python
[{'name': 'Item-2', 'price': 555.22}]
```

This function works by first sorting the items by price in descending order. The `sort` function uses a lambda function as the key to sort the items. The `reverse=True` argument tells `sort` to sort in descending order. Finally, the function returns the first `n` items from the sorted list.
