def make_a_pile(n):
    pile = [n]
    stones = n
    for i in range(1, n):
        if n % 2 == 0:
            stones += 2
        else:
            stones += 1
        pile.append(stones)
    return pile
