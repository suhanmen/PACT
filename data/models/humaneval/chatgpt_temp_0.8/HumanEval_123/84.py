def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    collatz_seq = [n]  # start with n as the first term in the sequence
    while n != 1:  # continue until we reach 1 (the end of the sequence)
        if n % 2 == 0:  # if n is even
            n //= 2   # divide it by 2
        else:  # if n is odd
            n = n * 3 + 1  # multiply it by 3 and add 1
        collatz_seq.append(n)  # add the new term to the sequence
    
    # filter the odd numbers from the collatz sequence
    odd_numbers = [num for num in collatz_seq if num % 2 == 1]
    
    return sorted(odd_numbers)  # sort the odd numbers in increasing order and return the list
