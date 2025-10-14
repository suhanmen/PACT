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

    collatz_seq = [n] # Start with the given number
    while n != 1: # Keep generating the sequence until we reach 1
        if n % 2 == 0: # If previous term is even
            n = n // 2 # Next term is half of previous term
        else: # If previous term is odd
            n = (3 * n) + 1 # Next term is 3 times previous term plus 1
        collatz_seq.append(n) # Add the next term to the sequence
    
    # Filter the sequence to only contain odd numbers
    odd_numbers = [x for x in collatz_seq if x % 2 != 0]
    
    # Sort the odd numbers in increasing order and return the list
    return sorted(odd_numbers)
