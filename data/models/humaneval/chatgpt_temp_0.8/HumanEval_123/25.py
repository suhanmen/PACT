def get_odd_collatz(n):
    collatz = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz.append(n)
    return sorted(list(set(filter(lambda x: x % 2 == 1, collatz))))
