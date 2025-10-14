def tri(n):
    sequence = [3] # initialize the sequence with the first term
    if n == 0:
        return sequence[:1] # return only the first term
    elif n == 1:
        return sequence[:2] # return the first two terms
    else:
        for i in range(2, n + 1):
            if i % 2 == 0:
                sequence.append(1 + i // 2)
            else:
                sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
        return sequence
