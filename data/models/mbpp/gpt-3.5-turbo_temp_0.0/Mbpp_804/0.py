Here is the completed code snippet:

```python
def is_product_even(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product % 2 == 0

assert is_product_even([1,2,3])
```

In this code, we define a function `is_product_even` that takes a list of numbers as input. We initialize a variable `product` to 1, and then iterate over each number in the list. For each number, we multiply it with the current value of `product`. After iterating through all the numbers, we check if the product is divisible by 2 (i.e., if it is even) by using the modulo operator `%`. If the product is even, the function returns `True`, otherwise it returns `False`.

The `assert` statement at the end of the code snippet is used to verify that the function behaves as expected. In this case, it checks if the product of the numbers `[1,2,3]` is even, and if not, it will raise an `AssertionError`.