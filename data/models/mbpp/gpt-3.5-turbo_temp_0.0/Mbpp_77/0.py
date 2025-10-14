Here is the completed code snippet:

```python
def is_Diff(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Calculate the sum of the digits at even positions
    even_sum = 0
    for i in range(1, len(number_str), 2):
        even_sum += int(number_str[i])
    
    # Calculate the sum of the digits at odd positions
    odd_sum = 0
    for i in range(0, len(number_str), 2):
        odd_sum += int(number_str[i])
    
    # Calculate the difference between the sums
    diff = abs(even_sum - odd_sum)
    
    # Check if the difference is divisible by 11
    if diff % 11 == 0:
        return True
    else:
        return False

# Test the function
assert is_Diff(12345) == False
```

The function `is_Diff` takes a number as input and checks if the difference between the sum of the digits at even positions and the sum of the digits at odd positions is divisible by 11. If the difference is divisible by 11, the function returns `True`, otherwise it returns `False`. The provided test case checks if the function returns `False` for the number 12345.