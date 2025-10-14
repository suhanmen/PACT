"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""



def rearrange_bigger(n):
    # Convert the number to a list of its digits
    digits = list(str(n))
    length = len(digits)
    
    # Start from the end of the list and find the first digit
    # that is smaller than the digit next to it.
    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else: # If no such digit is found, the number is the highest possible with its digits.
        return -1
    
    # Find the smallest digit on right side of (i) that is greater than digits[i]
    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            break
    
    # Swap the found digits
    digits[i], digits[j] = digits[j], digits[i]
    
    # Rearrange the remaining digits in ascending order
    digits[i + 1:] = sorted(digits[i + 1:])
    
    # Convert the list of digits back to an integer
    return int(''.join(digits))

# Example usage:
# assert rearrange_bigger(12) == 21
