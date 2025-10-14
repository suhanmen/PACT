def tri(n):
    tri_sequence = [3]
    if n == 0:
        return tri_sequence
    prev1, prev2, prev3 = 2, 1, 3
    for i in range(1, n+1):
        if i % 2 == 0:
            tri_sequence.append(1 + i // 2)
        else:
            current = prev1 + prev2 + prev3
            tri_sequence.append(current)
            prev1, prev2, prev3 = prev2, prev3, current
    return tri_sequence
