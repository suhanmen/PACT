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
    sequence = [3]  # initialize sequence with first term (tri(1) = 3)
    if n == 0:  # if n is 0, return empty list
        return []
    elif n == 1:  # if n is 1, return sequence with first term only
        return sequence
    elif n == 2:  # if n is 2, return sequence with first two terms
        sequence.append(1 + n//2)
        return sequence
    else:  # for n >= 3, calculate and append remaining terms to sequence
        sequence.append(1 + n//2)
        for i in range(3, n+1):
            if i % 2 == 0:  # if i is even
                sequence.append(1 + i//2)
            else:  # if i is odd
                sequence.append(sequence[i-2] + sequence[i-3] + sequence[i])
        return sequence
