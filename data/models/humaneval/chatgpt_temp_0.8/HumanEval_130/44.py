def tri(n):
    sequence = [3] * (n+1)  # initialize sequence with first two values
    if n >= 1:
        sequence[1] = 1
    for i in range(2, n+1):
        if i % 2 == 0:
            sequence[i] = 1 + i // 2
        else:
            sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i+1]
    return sequence
