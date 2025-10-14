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

    # Initialize a list to hold the sequence
    sequence = []

    # Base case: tri(1) = 3
    if n == 0:
        sequence.append(0)
        return sequence
    elif n == 1:
        sequence.append(3)
        return sequence
    elif n == 2:
        sequence.append(1)
        sequence.append(3)
        sequence.append(2)
        return sequence

    # Initialize the first three numbers of the sequence
    a, b, c = 1, 3, 2
    sequence.append(a)
    sequence.append(b)
    sequence.append(c)

    # Compute the rest of the sequence
    for i in range(3, n+1):
        if i % 2 == 0:
            # Even case: tri(n) = 1 + n / 2
            tri = 1 + (i / 2)
        else:
            # Odd case: tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1)
            tri = sequence[-1] + sequence[-2] + sequence[-4]
        sequence.append(tri)

    return sequence
