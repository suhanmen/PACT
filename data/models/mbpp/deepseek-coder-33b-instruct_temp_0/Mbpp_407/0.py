Here is the Python function to create the next bigger number by rearranging the digits of a given number:

```python
def rearrange_bigger(n):
    # Convert the number to a list of digits
    digits = list(str(n))
    
    # Find the pivot point where the digit is smaller than the next one from the right
    pivot = len(digits) - 2
    while pivot >= 0 and digits[pivot] >= digits[pivot + 1]:
        pivot -= 1
    
    # If no such pivot point exists, the number cannot be rearranged to a bigger one
    if pivot == -1:
        return -1
    
    # Find the smallest digit that is greater than the pivot digit
    successor = len(digits) - 1
    while digits[successor] <= digits[pivot]:
        successor -= 1
    
    # Swap the pivot digit and the successor digit
    digits[pivot], digits[successor] = digits[successor], digits[pivot]
    
    # Reverse the digits to the right of the pivot
    digits[pivot + 1:] = reversed(digits[pivot + 1:])
    
    # Convert the list of digits back to a number
    return int(''.join(digits))
```

This function works by finding the pivot point where the digit is smaller than the next one from the right. If no such pivot point exists, the number cannot be rearranged to a bigger one. If a pivot point is found, the function finds the smallest digit that is greater than the pivot digit, swaps them, and reverses the digits to the right of the pivot. The function then converts the list of digits back to a number and returns it.
