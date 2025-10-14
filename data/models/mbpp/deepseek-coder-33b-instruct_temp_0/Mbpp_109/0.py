Here is the Python function to solve the problem:

```python
def odd_Equivalent(binary_string, num_rotations):
    # Convert the binary string to a list of integers
    binary_list = [int(digit) for digit in binary_string]

    # Rotate the list num_rotations times
    for _ in range(num_rotations):
        # Pop the last element and insert it at the beginning
        binary_list.insert(0, binary_list.pop())

    # Count the number of odd numbers in the rotated list
    odd_count = sum(1 for num in binary_list if num % 2 != 0)

    return odd_count
```

You can test the function with the given example:

```python
print(odd_Equivalent("011001", 6))  # Output: 3
```

This function works by first converting the binary string to a list of integers. Then, it rotates the list by popping the last element and inserting it at the beginning of the list for the given number of times. Finally, it counts the number of odd numbers in the rotated list and returns this count.
