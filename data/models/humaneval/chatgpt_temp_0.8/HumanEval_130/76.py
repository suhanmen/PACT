def tri(n):
    sequence = [3]
    if n == 0:
        return sequence
    elif n >= 1:
        sequence.append(1 + n // 2)
    for i in range(3, n + 2):
        if i % 2 == 1:
            sequence.append(sequence[i - 3] + sequence[i - 4] + sequence[i - 1])
        else:
            sequence.append(1 + i // 2)
    return sequence
