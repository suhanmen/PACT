def get_odd_collatz(n):
    collatz_seq = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        collatz_seq.append(n)
    odd_collatz_seq = sorted(list(set(filter(lambda x: x % 2 != 0, collatz_seq)))))
    return odd_collatz_seq
