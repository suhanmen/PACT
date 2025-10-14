Here's the completed code snippet:

```python
def rearrange_bigger(number):
    # Convert the number to a list of digits
    digits = list(str(number))
    
    # Find the first digit from the right that is smaller than its next digit
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i+1]:
        i -= 1
    
    # If no such digit is found, the number is already the largest possible
    if i == -1:
        return number
    
    # Find the smallest digit to the right of digits[i] that is larger than digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]
    
    # Reverse the digits to the right of digits[i]
    digits[i+1:] = digits[i+1:][::-1]
    
    # Convert the list of digits back to a number and return it
    return int(''.join(digits))
```

This function uses a modified version of the "next permutation" algorithm to find the next bigger number by rearranging the digits. It first finds the first digit from the right that is smaller than its next digit. Then, it finds the smallest digit to the right of that digit that is larger than it. It swaps these two digits and then reverses the digits to the right of the first digit. Finally, it converts the list of digits back to a number and returns it.