def get_odd_collatz(n):
    seq = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        seq.append(n)
    odd_seq = sorted(list(set(filter(lambda x: x % 2 == 1, seq)))))
    if odd_seq[0] == 1:
        return odd_seq
    else:
        return [1] + odd_seq
