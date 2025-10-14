def get_odd_collatz(n):
    collatz = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        collatz.append(n)
    return sorted(set(filter(lambda x: x % 2 == 1, collatz)))
