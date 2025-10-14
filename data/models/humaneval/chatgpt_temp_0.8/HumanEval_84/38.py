def solve(N):
    # Convert the integer to binary and remove the '0b' prefix
    binary = bin(N)[2:]
    
    # Sum up the digits in the binary representation
    digit_sum = sum(int(digit) for digit in binary)
    
    # Convert the digit sum to a binary string and return it
    return bin(digit_sum)[2:]
