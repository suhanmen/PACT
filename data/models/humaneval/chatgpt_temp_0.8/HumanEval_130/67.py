def tri(n):
    seq = [3]
    if n == 0:
        return seq
    elif n == 1:
        seq.append(1 + (n / 2))
        return seq
    else:
        seq.append(1 + (2 / 2))
        for i in range(2, n+1):
            if i % 2 == 0:
                seq.append(1 + (i / 2))
            else:
                seq.append(seq[i-1] + seq[i-2] + seq[i+1])
        return seq
