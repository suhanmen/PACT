def tri(n):
    """
    Returns a list of the first n + 1 numbers of the Tribonacci sequence.
    """
    tribonacci = [0]*(n+1)
    if n == 0:
        return [0]
    tribonacci[1] = 3
    if n > 1:
        tribonacci[2] = 2
    for i in range(3, n+1):
        if i % 2 == 0:
            tribonacci[i] = 1 + i // 2
        else:
            tribonacci[i] = tribonacci[i-1] + tribonacci[i-2] + tribonacci[i+1]

    return tribonacci
