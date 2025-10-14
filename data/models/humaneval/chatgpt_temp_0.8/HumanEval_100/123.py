def make_a_pile(n):
    pile = [n]      # Start with n stones in the first level
    for i in range(1, n):
        if n % 2 == 0:
            next_stones = n + 2*i  # If n is even, add 2 stones each time
        else:
            next_stones = n + 2*i - 1  # If n is odd, add 1 stone each time
        pile.append(next_stones)
    return pile
