Here is the Python function implemented in a markdown style code block:

```python
def sum_of_digits(lst):
    total = 0
    for num in lst:
        for digit in str(num):
            total += int(digit)
    return total
```

You can test the function with the following code:

```python
print(sum_of_digits([10,2,56]))  # Output: 14
```

This function works by iterating over each number in the list, converting it to a string to be able to iterate over its digits, and then adding each digit to a total sum. The total sum is then returned.
