def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isnumeric():
            num = int(digit)
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    primes.append(digit)
                    count += 1
    return count
