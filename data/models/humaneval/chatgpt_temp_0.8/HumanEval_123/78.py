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

    # Initialize the sequence with the given number n
    sequence = [n]

    # While the last element in the sequence is not 1, continue the sequence
    while sequence[-1] != 1:
        # Get the next element in the sequence based on whether the current one is even or odd
        if sequence[-1] % 2 == 0:
            next_number = sequence[-1] // 2
        else:
            next_number = 3*sequence[-1] + 1
        # Add the next number to the sequence
        sequence.append(next_number)

    # Filter only the odd numbers from the sequence
    odd_numbers = list(filter(lambda x: x % 2 == 1, sequence))

    # Return the list of odd numbers in increasing order
    return sorted(odd_numbers)
