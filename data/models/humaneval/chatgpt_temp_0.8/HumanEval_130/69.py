def tri(n):
    sequence = [3] # initialize the sequence with the first number
    if n == 0:
        return sequence # if n is 0, return the sequence with only the first number
    a, b, c = 1, 1, 3 # initialize the variables for calculating the sequence
    for i in range(1, n+1):
        if i % 2 == 0: # if i is even, use the formula for even numbers
            next_num = 1 + i // 2
        else: # if i is odd, use the formula for odd numbers
            next_num = a + b + c
            a, b, c = b, c, next_num # update the variables for calculating the sequence
        sequence.append(next_num) # add the next number to the sequence
    return sequence
