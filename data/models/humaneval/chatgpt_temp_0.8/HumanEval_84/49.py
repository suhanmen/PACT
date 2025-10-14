def solve(N):
    # Convert the integer to a string so we can iterate over its digits
    digits = str(N)
    # Initialize a variable to store the sum of digits in binary
    binary_sum = 0
    # Iterate over each digit in the string
    for digit in digits:
        # Convert the digit to an integer and add it to the binary sum
        binary_sum += int(digit)
    # Convert the binary sum to a binary string and return it
    return bin(binary_sum)[2:]
