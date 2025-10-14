Here is the Python function to find the n'th Lucas number:

```python
def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        lucas_numbers = [2, 1]
        for i in range(2, n+1):
            lucas_numbers.append(lucas_numbers[i-1] + lucas_numbers[i-2])
        return lucas_numbers[n]

# Test the function
print(find_lucas(9))  # Output: 76
```

This function uses a list to store the Lucas numbers as it calculates them. The first two Lucas numbers are 2 and 1, and each subsequent number is the sum of the two preceding ones. The function returns the n'th Lucas number.
