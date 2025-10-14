def solve(N):
    # Convert N to a string and then to a list of digits
    digits = [int(d) for d in str(N)]
    
    # Sum the digits and convert to binary
    binary_sum = bin(sum(digits))[2:]
    
    return binary_sum
