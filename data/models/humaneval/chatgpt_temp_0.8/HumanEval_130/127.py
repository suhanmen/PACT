def tri(n):
    sequence = [3]
    i = 1
    while len(sequence) < n + 1:
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
        i += 1
    return sequence
