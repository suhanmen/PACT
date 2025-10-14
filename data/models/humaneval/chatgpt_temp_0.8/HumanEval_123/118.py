def get_odd_collatz(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sorted(set(filter(lambda x: x % 2 == 1, sequence)))
