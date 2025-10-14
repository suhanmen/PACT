def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    cnt = 0
    for digit in num:
        if digit in primes:
            cnt += 1
        elif digit.isdigit():
            n = int(digit)
            if n > 1:
                for i in range(2, n):
                    if n % i == 0:
                        break
                else:
                    primes.append(digit)
                    cnt += 1
    return cnt
