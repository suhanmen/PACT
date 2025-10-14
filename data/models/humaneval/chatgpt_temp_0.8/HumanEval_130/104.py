def tri(n):
    sequence = [3] # initialize the sequence with tri(1) = 3
    for i in range(2, n+2):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            sequence.append(sequence[i-2] + sequence[i-3] + sequence[i])
    return sequence[:n+1]
