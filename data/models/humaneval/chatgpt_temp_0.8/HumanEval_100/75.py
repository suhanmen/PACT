def make_a_pile(n):
    pile = [n]
    for i in range(1, n):
        if n % 2 == 0:
            pile.append(n + i*2)
        else:
            pile.append(n + i*2 - 1)
    return pile
