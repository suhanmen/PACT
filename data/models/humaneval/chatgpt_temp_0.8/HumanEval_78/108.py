def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif int(digit, 16) > 17:
            for i in range(2, int(int(digit, 16)**(1/2))+1):
                if int(digit, 16) % i == 0:
                    break
            else:
                count += 1
    return count
