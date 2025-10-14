def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isalpha() and int(digit, 16) > 13:
            for i in range(2, int(int(digit, 16) ** 0.5) + 1):
                if int(digit, 16) % i == 0:
                    break
            else:
                primes.append(digit)
                count += 1
    return count
