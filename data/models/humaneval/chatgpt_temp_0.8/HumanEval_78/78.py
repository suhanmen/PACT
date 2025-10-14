def hex_key(num):
    count = 0
    primes = ['2', '3', '5', '7', 'B', 'D']
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isnumeric():
            n = int(digit)
            if n > 1:
                for i in range(2, n):
                    if n % i == 0:
                        break
                else:
                    count += 1
    return count
