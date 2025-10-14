def tri(n):
    sequence = [3] # The first number of the sequence is always 3
    a, b, c = 0, 0, 3 # Initialize the variables for the recurrence
    for i in range(n):
        if i == 0:
            a = 0
        elif i == 1:
            b = 0
        elif i == 2:
            c = 1
        elif i % 2 == 0:
            c = 1 + i // 2
        else:
            a, b, c = b, c, sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(c)
    return sequence
