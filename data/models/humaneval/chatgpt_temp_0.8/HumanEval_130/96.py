def tri(n):
    """
    Returns the first n + 1 numbers of the Tribonacci sequence.
    """
    sequence = [3]  # first number in the sequence is 3

    # loop through the remaining n numbers and calculate the next number in the sequence
    for i in range(1, n+1):
        if i % 2 == 0:
            next_num = 1 + i // 2
        else:
            next_num = sequence[i-1] + sequence[i-2] + sequence[i+1]
        sequence.append(next_num)

    return sequence
