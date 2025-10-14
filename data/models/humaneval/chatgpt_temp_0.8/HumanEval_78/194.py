def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for n in num:
        if n in primes:
            count += 1
        elif n.isdigit():
            if int(n) > 1:
                for i in range(2, int(n)):
                    if int(n) % i == 0:
                        break
                else:
                    count += 1
    return count
