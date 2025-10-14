Here is the completed code snippet:

```python
def find_remainder(arr, n):
    product = 1
    for num in arr:
        product *= num
        product %= n
    return product

assert find_remainder([100, 10, 5, 25, 35, 14], 11) == 9
```

In this code, the `find_remainder` function takes in an array `arr` and a number `n`. It initializes a variable `product` to 1. Then, it iterates over each number in the array and multiplies it with the current value of `product`. After each multiplication, it takes the modulo `n` of the product to ensure that the result remains within the range of `n`. Finally, it returns the product modulo `n`.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `find_remainder([100, 10, 5, 25, 35, 14], 11)` is equal to 9. If the assertion fails, an error will be raised.