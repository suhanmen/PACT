def make_a_pile(n):
    pile = [n]
    for i in range(2, n+1):
        if n % 2 == 0:
            pile.append(n + i)
        else:
            pile.append(n + (i-1))
    return pile
