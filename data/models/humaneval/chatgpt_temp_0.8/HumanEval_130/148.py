def tri(n):
    seq = [3]
    if n == 0:
        return seq
    elif n == 1:
        return seq + [1]
    elif n == 2:
        return seq + [1, 2]
    else:
        seq += [1, 1, 2]
        for i in range(3, n+1):
            if i % 2 == 0:
                seq.append(1 + i // 2)
            else:
                seq.append(seq[-1] + seq[-2] + seq[-5])
        return seq
