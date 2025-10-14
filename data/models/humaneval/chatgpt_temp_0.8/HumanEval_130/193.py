def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    sequence = [3]  # initialize the sequence with the first term
    if n > 0:
        sequence.append(1)  # append the second term if n is positive
    if n > 1:
        sequence.append(1)  # append the third term if n is greater than 1
    for i in range(3, n+1):  # loop to compute remaining terms in the sequence
        if i % 2 == 0:  # if i is even
            sequence.append(1 + i // 2)
        else:  # if i is odd
            sequence.append(sequence[i-1] + sequence[i-2] + sequence[i+1])
    return sequence
