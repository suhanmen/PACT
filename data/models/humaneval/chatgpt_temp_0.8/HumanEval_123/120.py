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

    # Create an empty list to store the odd numbers in the collatz sequence
    odd_numbers = []

    # If n is equal to 1, return [1] as the collatz sequence
    if n == 1:
        return [1]

    # While n is greater than 1
    while n > 1:
        # If n is odd, add it to the odd_numbers list
        if n % 2 == 1:
            odd_numbers.append(n)
        # Calculate the next term in the collatz sequence
        n = n * 3 + 1 if n % 2 == 1 else n // 2

    # Add 1 to the odd_numbers list
    odd_numbers.append(1)

    # Sort the odd_numbers list in increasing order and return it
    return sorted(odd_numbers)
