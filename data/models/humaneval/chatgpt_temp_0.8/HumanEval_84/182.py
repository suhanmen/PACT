def solve(N):
    # Convert N to binary string and then to list of digits
    binary_digits = list(bin(N)[2:])
    # Calculate the sum of binary digits
    binary_sum = sum(map(int, binary_digits))
    # Convert binary_sum to binary string and return it
    return bin(binary_sum)[2:]
