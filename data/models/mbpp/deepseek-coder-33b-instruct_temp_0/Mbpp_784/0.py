Here is the Python function to find the product of first even and odd number of a given list:

```python
def mul_even_odd(lst):
    even = next((x for x in lst if x % 2 == 0), None)
    odd = next((x for x in lst if x % 2 != 0), None)
    if even is not None and odd is not None:
        return even * odd
    else:
        return None
```

This function uses Python's built-in `next` function with a generator expression to find the first even and odd number in the list. If both an even and odd number are found, it returns their product. If either an even or odd number is not found, it returns `None`.

You can test this function with the provided test case:

```python
print(mul_even_odd([1,3,5,7,4,1,6,8]))  # Output: 4
```

This will output `4`, which is the product of the first even number `4` and the first odd number `1` in the list.
