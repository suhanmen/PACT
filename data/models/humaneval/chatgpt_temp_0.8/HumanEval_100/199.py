def make_a_pile(n):
    piles = []
    for i in range(n):
        pile_size = n + 2*i if n % 2 == 1 else n + 1 + 2*i
        piles.append(pile_size)
    return piles
