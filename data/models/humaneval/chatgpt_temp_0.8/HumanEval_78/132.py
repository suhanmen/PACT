def hex_key(num):
    primes = ["2", "3", "5", "7", "B", "D"]  # list of prime hex digits
    count = 0  # counter variable to keep track of prime digits
    for digit in num:
        if digit in primes:
            count += 1
    return count
