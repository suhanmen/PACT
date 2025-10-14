def hex_key(num):
    hex_primes = ["2", "3", "5", "7", "B", "D"]
    count = 0
    for digit in num:
        if digit in hex_primes:
            count += 1
    return count
