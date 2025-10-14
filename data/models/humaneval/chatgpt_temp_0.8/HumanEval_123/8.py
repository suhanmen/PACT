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

    # Define the list to store the odd numbers in the sequence
    odd_numbers = []

    # Add the starting number n to the sequence
    sequence = [n]

    # Continue to generate the sequence until it reaches 1
    while sequence[-1] != 1:

        # Determine the next number in the sequence according to the Collatz conjecture
        if sequence[-1] % 2 == 0:
            next_number = sequence[-1] // 2
        else:
            next_number = sequence[-1] * 3 + 1

        # Add the next number to the sequence
        sequence.append(next_number)

        # If the next number is odd, add it to the list of odd numbers
        if next_number % 2 == 1:
            odd_numbers.append(next_number)

    # Add 1 to the list of odd numbers as it is always in the sequence
    odd_numbers.append(1)

    # Sort and return the list of odd numbers
    return sorted(odd_numbers)
