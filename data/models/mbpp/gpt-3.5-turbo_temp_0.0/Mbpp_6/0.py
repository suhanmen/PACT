Here is the completed code snippet:

```python
def differ_At_One_Bit_Pos(num1, num2):
    # Convert the numbers to binary strings
    binary1 = bin(num1)[2:]
    binary2 = bin(num2)[2:]

    # Pad the binary strings with leading zeros if necessary
    binary1 = binary1.zfill(max(len(binary1), len(binary2)))
    binary2 = binary2.zfill(max(len(binary1), len(binary2)))

    # Count the number of differing bits
    count = 0
    for bit1, bit2 in zip(binary1, binary2):
        if bit1 != bit2:
            count += 1

    # Return True if the count is 1, indicating that the numbers differ at one bit position only
    return count == 1

assert differ_At_One_Bit_Pos(13, 9) == True
```

This function takes two numbers as input and converts them to binary strings. It then compares the binary strings bit by bit, counting the number of differing bits. If the count is equal to 1, it means that the numbers differ at one bit position only, so the function returns True. Otherwise, it returns False. The assert statement at the end verifies that the function works correctly for the given example.