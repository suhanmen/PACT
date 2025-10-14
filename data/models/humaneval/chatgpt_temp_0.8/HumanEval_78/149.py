def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif int(digit, 16) > 17 and int(digit, 16) % 2 != 0 and int(digit, 16) % 3 != 0:
            is_prime = True
            for i in range(5, int(int(digit, 16) ** 0.5) + 1, 6):
                if int(digit, 16) % i == 0 or int(digit, 16) % (i + 2) == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
    return count
