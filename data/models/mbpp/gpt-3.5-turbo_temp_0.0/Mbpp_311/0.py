Here's the completed code snippet:

```python
def set_left_most_unset_bit(num):
    # Convert the number to binary string
    binary = bin(num)[2:]

    # Find the index of the left most unset bit
    index = binary.find('0')

    # Set the left most unset bit to 1
    new_binary = binary[:index] + '1' + binary[index+1:]

    # Convert the binary string back to integer
    new_num = int(new_binary, 2)

    return new_num

assert set_left_most_unset_bit(10) == 14
```