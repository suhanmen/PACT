Here is the Python function to find the minimum product from the pairs of tuples within a given list:

```python
def min_product_tuple(lst):
    return min(x*y for x, y in lst)
```

This function uses a generator expression to calculate the product of each pair of numbers in the list, and then uses the `min` function to find the smallest product.

You can test this function with the provided test case:

```python
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))  # Output: 8
```

This will output `8`, which is the smallest product of pairs in the given list.
