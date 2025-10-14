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
    sequence = [3] * (n + 1)     # Initialize the sequence with the first element as 3
    if n == 0:                   # If n is 0, return an empty list
        return []
    elif n == 1:                 # If n is 1, return [3, 1]
        return [3, 1]
    elif n == 2:                 # If n is 2, return [3, 1, 2]
        return [3, 1, 2]
    for i in range(3, n + 1):    # For n > 2, calculate the next elements using the recurrence relation
        if i % 2 == 0:
            sequence[i] = 1 + i // 2
        else:
            sequence[i] = sequence[i - 1] + sequence[i - 2] + sequence[i + 1]
    return sequence
