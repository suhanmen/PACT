Here is the Python function implemented in a markdown style code block:

```python
def filter_oddnumbers(numbers):
    return [num for num in numbers if num % 2 != 0]

# Test the function
print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
```

This function uses list comprehension to iterate over the input list and only include numbers that are not divisible by 2 (i.e., odd numbers). The `%` operator is used to get the remainder of the division of `num` by 2. If the remainder is not 0, the number is odd.
