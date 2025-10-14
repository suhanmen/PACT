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

    # Initialize an empty list to store the odd numbers in the collatz sequence
    odd_nums = []

    # Initialize the collatz sequence with the input number
    collatz_seq = [n]

    # Loop until the sequence reaches 1
    while collatz_seq[-1] != 1:

        # Check if the previous term is even
        if collatz_seq[-1] % 2 == 0:
            # Next term is half of previous term
            next_term = collatz_seq[-1] // 2
        else:
            # Next term is 3 times the previous term plus 1
            next_term = 3 * collatz_seq[-1] + 1
        
        # Add the next term to the collatz sequence
        collatz_seq.append(next_term)
        
        # Check if the next term is odd
        if next_term % 2 != 0:
            # Add the odd number to the list
            odd_nums.append(next_term)

    # Add 1 to the list of odd numbers
    odd_nums.append(1)

    # Sort the list of odd numbers in increasing order
    odd_nums.sort()

    # Return the list of odd numbers
    r
