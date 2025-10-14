def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [3]
    else:
        seq = [3, 1]
        prev = 2
        curr = 0
        for i in range(2, n + 1):
            if i % 2 == 0:
                curr = prev + 1
            else:
                curr = seq[i - 1] + seq[i - 2] + seq[i + 1]
            seq.append(curr)
        return seq
