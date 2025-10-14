def tri(n):
    sequence = [3] * (n+1)
    if n == 0:
        return []
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 1]

    for i in range(3, n+1):
        if i % 2 == 0:
            sequence[i] = 1 + i // 2
        else:
            sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i+1]

    return sequence
