def tri(n):
    sequence = [3]
    if n == 0:
        return []
    elif n == 1:
        return sequence

    i = 1
    while i <= n:
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            sequence.append(sequence[i-1] + sequence[i-2] + sequence[i+1])
        i += 1
    return sequence
