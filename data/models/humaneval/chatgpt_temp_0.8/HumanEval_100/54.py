def make_a_pile(n):
    pile = [n]  # First level has n stones
    for i in range(n-1):  # Build the rest of the pile
        if n % 2 == 0:  # If n is even
            pile.append(pile[-1] + 2)  # Next level has two more stones
        else:  # If n is odd
            pile.append(pile[-1] + 1)  # Next level has one more stone
        n += 1  # Increment n
    return pile
