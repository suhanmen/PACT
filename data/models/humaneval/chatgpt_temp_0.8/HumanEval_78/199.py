def hex_key(num):
    primes = [2, 3, 5, 7, 11, 13, 17]
    hex_primes = ["2", "3", "5", "7", "B", "D"]
    count = 0
    for digit in num:
        if digit in hex_primes or int(digit, 16) in primes:
            count += 1
    return count
