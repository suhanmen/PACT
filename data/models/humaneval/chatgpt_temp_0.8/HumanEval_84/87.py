def solve(N):
    # Convert integer to string and then to binary
    binary = bin(N)[2:]

    # Calculate the sum of digits in binary
    sum_digits = sum([int(digit) for digit in binary])

    # Convert the sum to binary and return as string
    return bin(sum_digits)[2:]
