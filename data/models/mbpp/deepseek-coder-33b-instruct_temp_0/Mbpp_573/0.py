Here is the Python function to calculate the product of the unique numbers in a given list:

```python
def unique_product(lst):
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product
```

You can test the function with the provided test case:

```python
print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))  # Output: 720000000
```

This function works by first converting the input list to a set, which automatically removes any duplicate values. It then initializes a variable `product` to 1 and multiplies it by each number in the set. The final product is returned.
