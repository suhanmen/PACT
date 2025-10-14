def tri(n):
    sequence = [3]
    if n == 0:
        return sequence
    elif n == 1:
        sequence.append(1)
        return sequence
    elif n == 2:
        sequence.extend([1,2])
        return sequence
    else:
        sequence.extend([1,2])
        for i in range(3, n+1):
            if i % 2 == 0:
                sequence.append(1 + int(i/2))
            else:
                sequence.append(sequence[-1] + sequence[-2] + sequence[-4])
        return sequence
