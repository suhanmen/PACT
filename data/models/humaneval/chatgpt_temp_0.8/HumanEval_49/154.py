# CANNOT PARSE CODE SNIPPET
def modp(n: int, p: int) -> int:
    # Special case: 2^0 mod p = 1
    if n == 0:
        return 1
    
    # Compute 2^1 mod p, 2^2 mod p, etc.
    powers = [2 % p]
    for i in range(n.bit_length() - 1):
        powers.append((powers[-1] * powers[-1]) % p)
    
    # Reconstruct 2^n mod p from its binary representation
    result = 1
    for bit in bin(n)[2:]:
        if bit == '1':
            result = (result * powers.pop()) % p
        else:
            powers.pop()
    return result
