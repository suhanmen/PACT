def make_a_pile(n):
    pile = [n]
    stones = n
    for i in range(2, n+1):
        if n % 2 == 0:
            stones += 2
        else:
            stones += 1
        pile.append(stones)
    return pile
