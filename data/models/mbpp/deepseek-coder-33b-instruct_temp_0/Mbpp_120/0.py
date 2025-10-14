Here is the Python function to find the maximum absolute product between numbers in pairs of tuples within a given list:

```python
def max_product_tuple(lst):
    max_product = 0
    for tup in lst:
        product = abs(tup[0] * tup[1])
        if product > max_product:
            max_product = product
    return max_product
```

You can test the function with the provided test case:

```python
print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))  # Output: 36
```

This function works by iterating over each tuple in the list, calculating the absolute product of the two numbers in the tuple, and keeping track of the maximum product found so far. When it has checked all the tuples, it returns the maximum product.
