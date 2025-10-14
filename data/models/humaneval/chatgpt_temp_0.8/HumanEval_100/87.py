def make_a_pile(n):
    pile = [n]
    for i in range(n-1):
        if n % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
        n += 1
    return pile
