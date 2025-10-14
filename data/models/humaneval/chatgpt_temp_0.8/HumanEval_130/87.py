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
    seq = [0, 1, 1, 3]  # initialize sequence with the first three values
    
    for i in range(4, n+2):  # calculate and append the next values in the sequence
        if i % 2 == 0:
            seq.append(1 + i // 2)
        else:
            seq.append(seq[i-1] + seq[i-2] + seq[i+1])
            
    return seq[:n+1]  # return the first n+1 values in the sequence
