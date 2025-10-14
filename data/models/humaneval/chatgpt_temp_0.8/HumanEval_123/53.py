def get_odd_collatz(n):
    # Initialize the list with the starting number n
    collatz_seq = [n]

    # Keep generating more terms in the sequence until we reach 1
    while n > 1:
        if n % 2 == 0:
            # If the previous term is even, the next term is one half of the previous term
            n = n // 2
        else:
            # If the previous term is odd, the next term is 3 times the previous term plus 1
            n = 3 * n + 1
        collatz_seq.append(n)

    # Filter out the even numbers and return the odd numbers
    return sorted(filter(lambda x: x % 2 == 1, collatz_seq)))
