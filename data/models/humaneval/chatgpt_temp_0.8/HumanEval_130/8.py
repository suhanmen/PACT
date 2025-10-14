def tri(n):
    sequence = [3]
    if n == 0:
        return sequence
    elif n == 1:
        sequence.append(1)
        return sequence
    elif n == 2:
        sequence += [1, 2]
        return sequence
    else:
        sequence += [1, 2]
        n -= 2
        while n > 0:
            if (len(sequence) - 1) % 2 == 0:
                sequence.append(1 + (len(sequence) - 1) // 2)
            else:
                sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
            n -= 1
        return sequence
