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
    sequence = [3]  # Initialize sequence with the first number
    if n == 0:
        return sequence  # Return sequence with only the first number
    elif n == 1:
        sequence.append(1)  # Add second number to sequence
    elif n == 2:
        sequence.extend([1, 2])  # Add second and third numbers to sequence
    else:
        sequence.extend([1, 2])  # Add second and third numbers to sequence
        for i in range(3, n+1):
            if i % 2 == 0:
                sequence.append(1 + i // 2)  # Calculate even terms
            else:
                sequence.append(sequence[i-1] + sequence[i-2] + sequence[i+1])  # Calculate odd terms
    return sequence
