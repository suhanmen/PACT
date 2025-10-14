def get_odd_collatz(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        if n % 2 == 1:
            result.append(n)
    return sorted(result)
