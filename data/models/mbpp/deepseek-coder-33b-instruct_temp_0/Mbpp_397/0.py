Here is the Python function to find the median of three numbers:

```python
def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]

# Test the function
print(median_numbers(25,55,65))  # Output: 55.0
```

This function works by first creating a list of the three numbers, then sorting that list. The median of a sorted list of numbers is the middle number, which is why we return `numbers[1]`.
