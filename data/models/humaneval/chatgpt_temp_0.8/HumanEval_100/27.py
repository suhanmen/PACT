def make_a_pile(n):
    pile = [n]
    stones = n
    for i in range(1, n):
        if stones % 2 == 0:
            stones += 1
        else:
            stones += 2
        pile.append(stones)
    return pile
