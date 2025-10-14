def tri(n):
    sequence = [3]
    if n == 0:
        return sequence
    elif n == 1:
        sequence.append(1 + 1/2)
        return sequence
    elif n == 2:
        sequence.append(1 + 2/2)
        sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
        return sequence
    else:
        sequence.append(1 + 2/2)
        sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
        for i in range(3, n+1):
            if i % 2 == 0:
                sequence.append(1 + i/2)
            else:
                sequence.append(sequence[-1] + sequence[-2] + sequence[-4])
        return sequence
