Here is the Python function to find the product of the array multiplication modulo n:

```python
def find_remainder(arr, n):
    product = 1
    for i in arr:
        product *= i
        product %= n
    return product
```

You can test the function with the given test case:

```python
print(find_remainder([100, 10, 5, 25, 35, 14], 11))  # Output: 9
```

This function works by initializing a variable `product` to 1, then iterating over each element in the input array. For each element, it multiplies the current product by the element and takes the modulus of the result with `n`. The result is then returned as the final product.
