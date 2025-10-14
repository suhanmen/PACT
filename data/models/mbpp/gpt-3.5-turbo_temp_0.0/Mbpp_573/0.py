Here is the completed code snippet:

```python
def unique_product(numbers):
    unique_numbers = set(numbers)
    product = 1
    for num in unique_numbers:
        product *= num
    return product

assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000
```