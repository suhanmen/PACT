def hex_key(num):
    primes = ["2", "3", "5", "7", "B", "D"]
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isdigit():
            decimal = int(digit, 16)
            if decimal == 11 or decimal == 13 or decimal == 17:
                count += 1
    return count
