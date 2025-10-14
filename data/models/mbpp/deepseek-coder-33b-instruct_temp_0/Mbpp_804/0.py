Here is the Python function implemented in a markdown style code block:

```python
def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0
```

This function works by initializing a variable `product` to 1, then iterating over each number in the input list `lst`, multiplying `product` by that number. After all numbers have been multiplied together, it checks if the product is even by using the modulus operator `%` to get the remainder when `product` is divided by 2. If the remainder is 0, that means `product` is even, so the function returns `True`. Otherwise, it returns `False`.
