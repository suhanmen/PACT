def hex_key(num):
    primes = set(["2", "3", "5", "7", "B", "D"])
    count = 0
    for c in num:
        if c in primes:
            count += 1
        elif c.isdigit():
            n = int(c)
            if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)):
                primes.add(c)
                count += 1
    return count
