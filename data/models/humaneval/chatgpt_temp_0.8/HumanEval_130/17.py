def tri(n):
    """
    Returns a list of the first n + 1 numbers of the Tribonacci sequence.
    """
    sequence = [0] * (n + 1)
    sequence[0] = 1
    if n > 0:
        sequence[1] = 1
    if n > 1:
        sequence[2] = 3
    for i in range(3, n + 1):
        if i % 2 == 0:
            sequence[i] = 1 + i // 2
        else:
            sequence[i] = sequence[i - 1] + sequence[i - 2] + sequence[i + 1]
    return sequence
