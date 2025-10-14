def tri(n):
    sequence = [3] # initialize the sequence with the first number
    if n == 0:
        return sequence # return the sequence with only the first number
    elif n == 1:
        sequence.append(1 + (n / 2)) # calculate the second number in the sequence
        return sequence # return the sequence with the first two numbers
    else:
        sequence.append(1 + (n / 2)) # calculate the second number in the sequence
        for i in range(2, n + 1): # loop through the remaining numbers in the sequence
            if i % 2 == 0: # if i is even
                sequence.append(1 + (i / 2)) # calculate the i-th number in the sequence
            else: # if i is odd
                sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i + 1]) # calculate the i-th number in the sequence
        return sequence # return the complete sequence
