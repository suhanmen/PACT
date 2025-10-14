def make_a_pile(n):
    pile = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones = n + i*2
        else:
            stones = n + i*2 - 1
        pile.append(stones)
    return pile
