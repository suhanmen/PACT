python
def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isalpha():
            dec = int(digit, 16)
            if dec == 11 or dec == 13:
                count += 1
    return count
