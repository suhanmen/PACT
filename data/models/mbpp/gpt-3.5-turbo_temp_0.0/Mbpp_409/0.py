Here is the completed code snippet:

```python
def min_product_tuple(lst):
    min_product = float('inf')
    for pair in lst:
        product = pair[0] * pair[1]
        if product < min_product:
            min_product = product
    return min_product

assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
```

In this code, the `min_product_tuple` function takes a list of tuples as input. It initializes the `min_product` variable to infinity. Then, it iterates over each pair of tuples in the list. For each pair, it calculates the product of the two elements and checks if it is smaller than the current minimum product. If it is, the `min_product` variable is updated. Finally, the function returns the minimum product found.

The `assert` statement at the end of the code snippet checks if the function returns the expected result for the given example input.