def tri(n):
    seq = [3]
    if n == 0:
        return seq
    seq.append(1 + n // 2)
    if n == 1:
        return seq
    seq.append(sum(seq))
    for i in range(3, n+1):
        if i % 2 == 0:
            seq.append(1 + i // 2)
        else:
            seq.append(seq[-1] + seq[-2] + seq[-3])
    return seq
