def tri(n):
    sequence = [3]
    if n == 0:
        return sequence
    elif n == 1:
        sequence.append(1 + (n / 2))
    else:
        sequence.extend([1 + (i / 2) for i in range(2, n+1, 2)])
        for i in range(3, n+1, 2):
            sequence.append(sequence[i-1] + sequence[i-2] + sequence[i+1])
    return sequence
