Here is the completed code snippet:

```python
def max_product_tuple(lst):
    max_product = float('-inf')
    for pair in lst:
        product = abs(pair[0] * pair[1])
        if product > max_product:
            max_product = product
    return max_product

assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
```

In this code, the `max_product_tuple` function takes a list of tuples as input. It initializes the `max_product` variable to negative infinity. Then, it iterates over each pair of tuples in the list. For each pair, it calculates the absolute product of the two numbers and stores it in the `product` variable. If the `product` is greater than the current `max_product`, it updates the `max_product` to the new value. Finally, it returns the `max_product` after iterating through all the pairs.

The `assert` statement at the end is used to verify that the function returns the expected result for the given example.