Here is the completed code snippet:

```python
def even_bit_set_number(num):
    # Convert the number to binary representation
    binary = bin(num)[2:]

    # Set all even bits to 1
    new_binary = ''
    for i in range(len(binary)):
        if i % 2 == 0:
            new_binary += '1'
        else:
            new_binary += binary[i]

    # Convert the binary back to decimal
    new_num = int(new_binary, 2)

    return new_num

assert even_bit_set_number(10) == 10
```

This function takes a number as input and sets all even bits of the number to 1. It does this by converting the number to its binary representation, iterating through each bit, and replacing the even bits with 1. Finally, it converts the modified binary back to decimal and returns the result. The assertion at the end verifies that the function returns the expected result for the given example.