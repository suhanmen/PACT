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
    sequence = [3] #initialize the sequence with the first element
    if n == 0:
        return sequence #return the sequence with just the first element if n is 0
    
    #initialize variables for the first 3 elements of the sequence
    a, b, c = 1, 1, 3
    
    #iterate n times to generate the next n elements of the sequence
    for i in range(n):
        if i % 2 == 0: #if i is even
            next_element = c + (i / 2) #calculate the next element based on the even formula
        else:
            next_element = a + b + c #calculate the next element based on the odd formula
            a, b, c = b, c, next_element #update the variables for the first 3 elements of the sequence
        sequence.append(next_element) #add the next element to the sequence
    
    return sequence #return the complete sequence
