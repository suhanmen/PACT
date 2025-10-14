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

    # Starting with the first term of the sequence
    seq = [n]

    # Keep iterating until we reach 1
    while seq[-1] != 1:

        # If the previous term is even, divide by 2
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] // 2)

        # If the previous term is odd, multiply by 3 and add 1
        else:
            seq.append(seq[-1] * 3 + 1)

    # Filter the odd numbers from the sequence
    odd_nums = [num for num in seq if num % 2 == 1]

    # Sort and return the odd numbers
    return sorted(odd_nums)
