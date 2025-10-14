def get_odd_collatz(n):
    seq = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq.append(n)

    odd_seq = [num for num in seq if num % 2 == 1]
    return sorted(odd_seq)
