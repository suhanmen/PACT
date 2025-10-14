def solve(N):
    # Convert N to a string and then to binary
    binary_n = bin(N)[2:]
    # Initialize sum to 0
    sum = 0
    # Loop through each character in binary_n
    for char in binary_n:
        # Convert the char to an integer and add it to sum
        sum += int(char)
    # Convert the sum to a binary string and return it
    return bin(sum)[2:]
