Here is the Python function to check whether the two numbers differ at one bit position only or not.

```python
def differ_At_One_Bit_Pos(num1, num2):
    # XOR the two numbers
    xor_result = num1 ^ num2

    # Count the number of set bits in the XOR result
    count = 0
    while xor_result:
        xor_result &= xor_result - 1
        count += 1

    # If there is only one set bit, return True
    return count == 1

# Test the function
print(differ_At_One_Bit_Pos(13,9))  # Output: True
```

This function works by XORing the two numbers. The XOR operation will set the bits in the result where the two numbers differ. If the two numbers differ at only one bit position, there will be exactly one set bit in the XOR result. The function then counts the number of set bits in the XOR result and returns True if there is exactly one set bit, and False otherwise.
